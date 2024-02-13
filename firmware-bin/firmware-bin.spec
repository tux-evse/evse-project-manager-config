Name: firmware-bin
Version: 1.0.0
Release: 1%{?dist}
Summary: Firmware Binaries 

License: MIT
URL: http://nourl.org

Source0: https://github.com/tux-evse/evse-project-manager-config/raw/main/firmware-bin/tiboot3.bin
Source1: https://github.com/tux-evse/evse-project-manager-config/raw/main/firmware-bin/tispl.bin
Source2: https://github.com/tux-evse/evse-project-manager-config/raw/main/firmware-bin/u-boot.img
Source3: https://github.com/tux-evse/evse-project-manager-config/raw/main/firmware-bin/am62-mcu-m4f0_0-fw

%description
This is firmware binaries.

%prep

%build

%install
%{__install} -d %{buildroot}/firmware
%{__install} -d %{buildroot}%{_prefix}%{_sharedstatedir}/uboot_firmware/
%{__install} -Dm644 %{SOURCE0} %{buildroot}%{_sharedstatedir}/uboot_firmware
%{__install} -Dm644 %{SOURCE1} %{buildroot}%{_sharedstatedir}/uboot_firmware
%{__install} -Dm644 %{SOURCE2} %{buildroot}%{_sharedstatedir}/uboot_firmware
%{__install} -Dm644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firmware/

%files
%dir %{_sharedstatedir}/uboot_firmware
%dir %{_prefix}/lib/firmware/
%{_sharedstatedir}/uboot_firmware/*
%{_prefix}/lib/firmware/*
%changelog
