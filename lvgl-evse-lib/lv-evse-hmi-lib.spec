%global debug_package %{nil}

Name: lvgl-evse-lib
Version: 0.0.1
Release: 5%{?dist}
Summary: LVGL for frame buffer lib

License: MIT
URL: https://github.com/tux-evse/lv-evse-hmi-lib
Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

BuildRequires: cmake
BuildRequires: gcc gcc-c++

%description
LVGL for frame buffer lib.

#---------------------------------------------
%package devel
Group:          Development/Libraries/C and C++
Summary:        LVGL for frame buffer lib

Requires: %{name} = %{version}

%description devel
LVGL for frame buffer lib devel.

%prep
%autosetup -p 1

%build
%cmake
%cmake_build

%install
%make_install

%files
%{_prefix}/lib64/*.so

%files devel
%dir %{_includedir}/lvgl
%{_includedir}/*
%{_prefix}/lib64/pkgconfig/lvgl.pc

%changelog
