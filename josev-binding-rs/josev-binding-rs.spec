%global debug_package %{nil}


Name:    josev-binding-rs
Version: 0.0.1
Release: 0%{?dist}
Summary: josev binding

License: MIT
URL: https://github.com/tux-evse/josev-binding-rs.git
Source0: %{name}-%{version}.tar.gz
Source1: vendor.tar.bz2
Source2: cargo_config

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/josev-binding-rs/manifest.yml
#Source11: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/josev-binding-rs/manifest-test.yml

BuildRequires:   rust >= 1.70
BuildRequires:   cargo >= 1.70
BuildRequires: afb-librust
BuildRequires: clang-devel


%description
josev binding.

%package test
Summary: %{name} binding test

Requires: %{name} = %{version}
Requires:afb-ui-devtools

%description test
%{name} binding test.

%prep
%autosetup -a1

mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
cargo build --offline --release --target %{_arch}-unknown-linux-gnu

%install
mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/lib
cp ./target/%{_arch}-unknown-linux-gnu/release/*.so %{buildroot}%{_prefix}/redpesk/%{name}/lib

mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/%{name}/.rpconfig/manifest.yml

#mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig
#cp %{SOURCE11} %{buildroot}%{_prefix}/redpesk/%{name}/test/.rpconfig/manifest.yml

#mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
#mkdir -p %{buildroot}%{_prefix}/redpesk/%{name}/test/bin
#cp ./afb-binding/etc/*.json %{buildroot}%{_prefix}/redpesk/%{name}/test/etc
#cp ./afb-binding/etc/*.sh %{buildroot}%{_prefix}/redpesk/%{name}/test/bin

%files
%dir %{_prefix}/redpesk/%{name}
%dir %{_prefix}/redpesk/%{name}/.rpconfig
%{_prefix}/redpesk/%{name}/.rpconfig/*
%dir %{_prefix}/redpesk/%{name}/lib
%{_prefix}/redpesk/%{name}/lib/*

#%files test
#%dir %{_prefix}/redpesk/%{name}/test
#%dir %{_prefix}/redpesk/%{name}/test/bin
#%{_prefix}/redpesk/%{name}/test/bin/*
#%dir %{_prefix}/redpesk/%{name}/test/etc
#%{_prefix}/redpesk/%{name}/test/etc/*
#%dir %{_prefix}/redpesk/%{name}/test/.rpconfig
#%{_prefix}/redpesk/%{name}/test/.rpconfig/*

%changelog
