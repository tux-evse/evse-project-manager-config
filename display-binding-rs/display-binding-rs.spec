%global debug_package %{nil}
#ExcludeArch: x86_64

Name: display-binding-rs
Version: 0.0.4+20231219+2+g0dd0d13
Release: 2%{?dist}
Summary: Binding template/demo interfacing lvgl-rclib-rs with libafb-rs micro service architecture.

License: Apache
URL: https://github.com/tux-evse/display-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.gz
Source2: cargo_config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/display-binding-rs/manifest.yml
Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/display-binding-rs/manifest-test.yml
Source12: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/display-binding-rs/start_binder.sh
Source13: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/display-binding-rs/binding-display.json
Source14: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/display-binding-rs/binder-test.json


%ifarch x86_64
BuildRequires:   rust-archive >= 1.70.0
%else
%NativeBuildRequires   rust-archive >= 1.70.0

%endif



BuildRequires: afb-librust
BuildRequires: clang-devel
BuildRequires: glibc-devel
BuildRequires: glibc-headers

BuildRequires: pkgconfig(lvgl)
BuildRequires: pkgconfig(json-c)

BuildRequires: lvgl-rclib-rs

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}

%description test
%{name} binding test.

%description
Binding template/demo interfacing lvgl-rclib-rs with libafb-rs micro service architecture.

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

cargo build --offline  --release --target %{_arch}-unknown-linux-gnu


%install
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/etc
cp %{SOURCE13}  %{buildroot}%{_prefix}/redpesk/%{name}-test/etc
cp %{SOURCE14}  %{buildroot}%{_prefix}/redpesk/%{name}-test/etc

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/.rpconfig
cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}-test/.rpconfig/manifest.yml

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}-test/bin
cp %{SOURCE12} %{buildroot}%{_prefix}/redpesk/%{name}-test/bin/start_binder.sh

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*

%files test
%dir %{_prefix}/redpesk/%{name}-test
%dir %{_prefix}/redpesk/%{name}-test/bin
%{_prefix}/redpesk/%{name}-test/bin/*
%dir %{_prefix}/redpesk/%{name}-test/etc
%{_prefix}/redpesk/%{name}-test/etc/*
%dir %{_prefix}/redpesk/%{name}-test/.rpconfig
%{_prefix}/redpesk/%{name}-test/.rpconfig/*

%changelog