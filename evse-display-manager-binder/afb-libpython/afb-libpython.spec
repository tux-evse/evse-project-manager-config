Name:           afb-libpython
#Hexsha: d9a6340b04da62fdd0f7c99093c33fee7a676572
Version:        1.0.2
Release:        3%{?dist}
License:        LGPLv3
Summary:        Abstraction of afb-libafb for integration with non C/C++
Group:          Development/Libraries/C and C++
Url:            https://git.ovh.iot/redpesk/redpesk-common/afb-libpython
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  afb-cmake-modules
BuildRequires:  pkgconfig(libafb) >= 5.0
BuildRequires:  pkgconfig(librp-utils) >= 0.0.3
BuildRequires:  pkgconfig(libafb-binder) >= 5.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-devel

%global debug_package %{nil}

%description
Exposes afb-libafb to the Python scripting language.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p build
%if 0%{?almalinux_ver} == 8
  cd build
  %cmake ..
%else
  %cmake -B build
%endif
%make_build -C build

%install
%make_install -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{python3_sitearch}/*.so
