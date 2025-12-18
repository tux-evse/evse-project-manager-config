%global debug_package %{nil}

Name: afb-mqtt-ext
Version: 0.0.1
Release: 0%{?dist}
Summary: AFB micro-service framework extension for MQTT

License: Apache
URL: https://github.com/tux-evse/afb-mqtt-ext.git
Source0: %{name}-%{version}.tar.gz

Source10: https://raw.githubusercontent.com/tux-evse/evse-project-manager-config/main/afb-mqtt-ext/manifest.yml

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(librp-utils) >= 0.0.3
BuildRequires: afb-cmake-modules
BuildRequires: afm-rpm-macros
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(libafb)
BuildRequires: pkgconfig(libafb-binder)
BuildRequires: pkgconfig(libmosquitto)

Requires: mosquitto

%description
AFB micro-service framework extention for MQTT.

%prep
%autosetup -p 1

%build
mkdir build
cd build
cmake ..
make

%install
cd build

mkdir -p %{buildroot}%{_prefix}/redpesk/afb-mqtt/lib
cp libafb-mqtt-ext.so %{buildroot}%{_prefix}/redpesk/afb-mqtt/lib
mkdir -p %{buildroot}%{_prefix}/redpesk/afb-mqtt/.rpconfig
cp %{SOURCE10} %{buildroot}%{_prefix}/redpesk/afb-mqtt/.rpconfig/manifest.yml

%clean

%files
%dir %{_prefix}/redpesk/afb-mqtt
%dir %{_prefix}/redpesk/afb-mqtt/lib
%dir %{_prefix}/redpesk/afb-mqtt/.rpconfig

%{_prefix}/redpesk/afb-mqtt
%{_prefix}/redpesk/afb-mqtt/lib
%{_prefix}/redpesk/afb-mqtt/lib/libafb-mqtt-ext.so

%{_prefix}/redpesk/afb-mqtt/.rpconfig/*

%changelog
