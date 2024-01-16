%global debug_package %{nil}
ExcludeArch: x86_64

Name: scard-binding-rs
Version: 0.0.0+20231117+173249+0+ge1f8b8f
Release: 1%{?dist}
Summary: scard binding

License: MIT
URL: https://github.com/tux-evse/scard-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

%ifarch x86_64
BuildRequires:   rust-archive >= 1.70.0
%else
%NativeBuildRequires   rust-archive >= 1.70.0
%endif

BuildRequires: afb-librust
BuildRequires: clang-devel
BuildRequires: sec-pcscd-client-devel
BuildRequires: librp-utils-headers
BuildRequires: json-c-devel
BuildRequires: uthash-devel
BuildRequires: pcsc-lite-devel

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/scard-binding-rs/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/scard-binding-rs/manifest-test.yml


%description
scard binding.

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}
Requires: afb-ui-devtools

%description test
%{name} binding test.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%ifarch aarch64
export PKG_CONFIG_DIR="${PKG_CONFIG_DIR}:$CROSS_ROOT/usr/lib64/pkgconfig"
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:$CROSS_ROOT/usr/lib64/pkgconfig"
export PKG_CONFIG=/usr/aarch64-linux-gnu/sys-root/usr/bin/pkgconf

mkdir -p ${HOME}/.cargo/
cat << EOF >> "${HOME}/.cargo/config"
[target.aarch64-unknown-linux-gnu]
linker = "aarch64-linux-gnu-gcc"
EOF
%endif

#build fix
mkdir -p gnu;
touch gnu/stubs-32.h
export C_INCLUDE_PATH="${C_INCLUDE_PATH}:$(pwd)"
#End build fix

cargo build --offline --release --target %{_arch}-unknown-linux-gnu --features rpm_build


%install

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml



mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc

cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
cp ./afb-binding/etc/*.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*

%files test
%dir %{_prefix}/redpesk/%{name}/test
%dir %{_prefix}/redpesk/%{name}/test/bin
%{_prefix}/redpesk/%{name}/test/bin/*
%dir %{_prefix}/redpesk/%{name}/test/etc
%{_prefix}/redpesk/%{name}/test/etc/*
%dir %{_prefix}/redpesk/%{name}/test/.rpconfig
%{_prefix}/redpesk/%{name}/test/.rpconfig/*

%changelog