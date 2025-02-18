
%global debug_package %{nil}

Name: tux-evse-board-configuration
Version: 2.0.3
Release: 1%{?dist}
Summary: Board config (net, wifi hotspot, firewall...)

License: GPLv3
URL: https://github.com/tux-evse/tux-evse-board-configuration.git
Source0: %{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires: systemd-rpm-macros

Requires: firewalld
Requires: NetworkManager
Requires: avahi
Requires: avahi-tools
Requires: avahi-autoipd
Requires: sec-pcscd-client-tool

%description
Dedicated for all Valeo Charger board config (net, firewall...)

%prep
%autosetup -p 1

%build

%install
#udev
%{__install} -Dm644 ./linux_udev_rules/10-tty-evse.rules %{buildroot}%{_udevrulesdir}/10-tty-evse.rules
%{__install} -Dm644 ./linux_udev_rules/20-rpmsg.rules %{buildroot}%{_udevrulesdir}/20-rpmsg.rules
%{__install} -Dm644 ./linux_udev_rules/30-pcscd.rules %{buildroot}%{_udevrulesdir}/30-pcscd.rules

# nfc module blacklisting
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
%{__install} -Dm644 ./linux_pcscd_usb/blacklist-libnfc.conf %{buildroot}%{_sysconfdir}/modprobe.d/

#Conf eth2
mkdir -p %{buildroot}%{_sysconfdir}/NetworkManager/conf.d/

# systemD units & scripts installs
%{__install} -Dm644 ./network/config-network.service %{buildroot}%{_unitdir}/config-network.service
%{__install} -Dm744 ./network/config-network.sh %{buildroot}%{_bindir}/config-network
%{__install} -Dm644 ./firewall/config-firewall.service %{buildroot}%{_unitdir}/config-firewall.service
%{__install} -Dm744 ./firewall/config-firewall.sh %{buildroot}%{_bindir}/config-firewall
%{__install} -Dm644 ./hotspot_wifi/config-hotspot.service %{buildroot}%{_unitdir}/config-hotspot.service
%{__install} -Dm744 ./hotspot_wifi/config-hotspot.sh %{buildroot}%{_bindir}/config-hotspot
%{__install} -Dm744 ./linux_pcscd_usb/config-usb.sh %{buildroot}%{_bindir}/config-usb
%{__install} -Dm744 ./linux_pcscd_usb/reset-demo.sh %{buildroot}%{_bindir}/reset-demo
%{__install} -Dm744 ./openssl/genssl-demo.sh %{buildroot}%{_bindir}/genssl-demo
%{__install} -Dm644 ./cynagora/cynagora-debug-configuration.service %{buildroot}%{_unitdir}/cynagora-debug-configuration.service
%{__install} -Dm744 ./cynagora/cynagora-debug-configuration.sh %{buildroot}%{_bindir}/cynagora-debug-configuration.sh

# captive portal install
mkdir -p %{buildroot}%{_prefix}/redpesk/captive_portal/
cp -R ./hotspot_wifi/captive_portal/* %{buildroot}%{_prefix}/redpesk/captive_portal/

%post
%systemd_post config-network.service
%systemd_post config-firewall.service
%systemd_post config-hotspot.service
%systemd_post cynagora-debug-configuration.service
%systemd_post mosquitto.service

systemctl enable config-network.service > /dev/null
systemctl enable config-firewall.service > /dev/null
systemctl enable config-hotspot.service > /dev/null
systemctl enable cynagora-debug-configuration.service > /dev/null
systemctl enable mosquitto.service > /dev/null

# disable dnf metadata expiration
repo_file=$(ls /etc/yum.repos.d/tux-evse*.repo >/dev/null)
if [ -n "$repo_file" ]; then
    if ! grep -q "metadata_expire=0" "$repo_file"; then
        echo "metadata_expire=0" >> "$repo_file"
    fi
fi

# openssl certificates for https binder
if ! [ -d "/usr/redpesk/genssl" ] ; then
    echo "OpenSSL certificates, keys... generating..."
    /usr/bin/genssl-demo
fi

%systemd_preun config-network.service
%systemd_preun config-firewall.service
%systemd_preun config-hotspot.service
%systemd_preun cynagora-debug-configuration.service

# remove getty on tty1 so that it does not conflict with touchscreen
systemctl mask getty@tty1.service

%postun
%systemd_postun_with_restart config-network.service
%systemd_postun_with_restart config-firewall.service
%systemd_postun_with_restart config-hotspot.service
%systemd_postun_with_restart cynagora-debug-configuration.service

%files
# some configuration files (usb, udev rules...)
%{_udevrulesdir}/10-tty-evse.rules
%{_udevrulesdir}/20-rpmsg.rules
%{_udevrulesdir}/30-pcscd.rules
%{_sysconfdir}/modprobe.d/blacklist-libnfc.conf

# script used for the NFC reader configuration
%{_bindir}/config-usb

# script used to stop/restart the full demo using the framework with user rp-owner.
%{_bindir}/reset-demo

# script for openssl certificates, keys generating (for https binder)
%{_bindir}/genssl-demo

#systemD services files
%{_unitdir}/config-network.service
%{_bindir}/config-network
%{_unitdir}/config-firewall.service
%{_bindir}/config-firewall
%{_unitdir}/config-hotspot.service
%{_bindir}/config-hotspot
%{_unitdir}/cynagora-debug-configuration.service
%{_bindir}/cynagora-debug-configuration.sh

# captive portal
%{_prefix}/redpesk/captive_portal/conf-captive-portal.json
%{_prefix}/redpesk/captive_portal/html/assets/tux-evsex250.png
%{_prefix}/redpesk/captive_portal/html/index.html
%{_prefix}/redpesk/captive_portal/html/style.css

%changelog
