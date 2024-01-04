#
# spec file for package afb-app-manager
#
%global afm_name       afm
%global afm_confdir    %{_sysconfdir}/%{afm_name}
%global afb_binding_dir %{_libdir}/afb
%global afm_units_root %{_prefix}/local/lib/systemd
%global rpmplugindir   %{_libdir}/rpm-plugins
%global redpeskdir     %{_prefix}/redpesk

%global afm_datadir    %{_datadir}/%{afm_name}
%global afm_appdir     %{redpeskdir}
%global afm_icondir    %{redpeskdir}/.icons

# redpesk users and group
%define _rp_owner_name     rp-owner
%define _rp_owner_id       1001
%define _rp_guest_name     rp-guest
%define _rp_guest_id       1002
%define _rp_group_name     users
%define _rp_group_id       100

Name:           afb-app-manager
#Hexsha: b059d0651b408cc9c31d0a81ec298c2f1ea96689
Version:        12.2.3+4+gb059d06
Release: 43%{?dist}
License:        GPLv3
Summary:        Micro service application manager
Group:          Development/Libraries/C and C++
URL:            https://github.com/redpesk-core/afb-app-manager
Source0:        %{name}-%{version}.tar.gz
Source1: 50-afm.preset
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xmlsec1)
BuildRequires:  pkgconfig(xmlsec1-gnutls)
# pkgconfig(xmlsec1-gnutls) do not require xmlsec1-gnutls!
BuildRequires:  xmlsec1-gnutls
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(afb-binding) >= 4
BuildRequires:  pkgconfig(librp-utils-static)
BuildRequires:  m4
BuildRequires:  gcc-c++
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pkgconfig(sec-lsm-manager)
BuildRequires:  rpm-plugins-devel
BuildRequires:  procps-ng-devel
Requires:       nss-localuser
Requires:       sec-lsm-manager
Requires:       afb-binder
Requires:       afb-client
Requires(post): /usr/bin/chgrp
Requires(post): /usr/bin/passwd
Requires(post): /usr/sbin/useradd
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires(post): systemd-units

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Framework for installing, uninstalling, running and stopping
micro services packaged as widgets.

%package devel
Group:          Development/Libraries/C and C++
Provides:       pkgconfig(afm-main) = %{version}
Summary:        Micro service application manager, development files

%description devel
Declaration of variables of interest for package connecting to
the manager for installing, uninstalling, running and stopping
micro services packaged as widgets.

%package rpm
Requires: rpm-libs
Requires: %{name} = %{version}
Summary:  redpesk rpm plugin

%description rpm
%summary

%prep
%autosetup -p1

%build
%cmake \
   -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc \
   -DUSE_LIBZIP=1 \
   -DUSE_SIMULATION=0 \
   -DUSE_SDK=0 \
   -DWITH_TOOLS=ON \
   -Dafm_name=%{afm_name} \
   -Dafm_confdir=%{afm_confdir} \
   -Dafm_datadir=%{afm_datadir} \
   -Dafm_units_root=%{afm_units_root} \
   -DUNITDIR_USER=/usr/lib/systemd/user \
   -DUNITDIR_SYSTEM=/usr/lib/systemd/system \
   -DAGL_DEVEL=1 \
   -DALLOW_NO_SIGNATURE=ON \
   -Drpm_plugin_dir=%{__plugindir} \
   -Drpm_macros_dir=%{_rpmmacrodir} \
   .
%cmake_build

%install
%cmake_install
%{__install} -d %{buildroot}%{afm_units_root}/system
%{__install} -d %{buildroot}%{afm_units_root}/system/multi-user.target.wants
%{__install} -d %{buildroot}%{afm_units_root}/system/afm-user-session@.target.wants
%{__install} -d %{buildroot}%{afm_units_root}/user
%{__install} -d %{buildroot}%{afm_units_root}/user/default.target.wants
%{__install} -d %{buildroot}%{afm_units_root}/user/sockets.target.wants
%{__install} -d %{buildroot}%{redpeskdir}
%{__install} -d %{buildroot}%{afm_datadir}
%{__install} -d %{buildroot}%{afm_appdir}
%{__install} -d %{buildroot}%{afm_icondir}
%{__install} -d %{buildroot}%{_presetdir}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_presetdir}
ln -sf %{_unitdir}/afm-user-session@.service %{buildroot}%{afm_units_root}/system/multi-user.target.wants/afm-user-session@%{_rp_owner_id}.service

%pre
getent group %{afm_name} > /dev/null || groupadd --system %{afm_name} ||:
getent passwd %{afm_name} > /dev/null || useradd --system --gid %{afm_name} --home-dir / %{afm_name} || :
getent group display > /dev/null || groupadd --system display ||:
getent passwd display > /dev/null || useradd --gid display --groups video,input --home-dir /run/platform/display --shell /bin/false --comment "Display daemon" --key PASS_MAX_DAYS=-1 display || :

%post
%systemd_post afm-system-setup.service afm-system-daemon.service afm-system-daemon.socket afmpkg-installer.service afmpkg-installer.socket

# Users creation
getent group %{_rp_group_name} > /dev/null || groupadd -g %{_rp_group_id} %{_rp_group_name} ||:
# The definition of the passwd is in a way secure because echo is a builtin command and will not be displayed with ps command.
# The definition of the password remains weak due to its complexity.
%{_libexecdir}/afm/afm-create-user.sh %{_rp_owner_id} %{_rp_owner_name} %{_rp_group_name} && echo %{_rp_owner_name} | passwd %{_rp_owner_name} --stdin ||:
%{_libexecdir}/afm/afm-create-user.sh %{_rp_guest_id} %{_rp_guest_name} %{_rp_group_name} && echo %{_rp_guest_name} | passwd %{_rp_guest_name} --stdin ||:

chgrp %{afm_name} %{afm_units_root}/system
chgrp %{afm_name} %{afm_units_root}/system/afm-user-session@.target.wants
chgrp %{afm_name} %{afm_units_root}/user/default.target.wants
chgrp %{afm_name} %{afm_units_root}/user/sockets.target.wants

chown %{afm_name}:%{afm_name} %{redpeskdir}
chown %{afm_name}:%{afm_name} %{afm_datadir}
chown %{afm_name}:%{afm_name} %{afm_appdir}
chown %{afm_name}:%{afm_name} %{afm_icondir}

if [ -x "/usr/bin/chsmack" ]
then
   chsmack -a 'System:Shared' -t %{afm_units_root}/system
   chsmack -a 'System:Shared' -t %{afm_units_root}/system/afm-user-session@.target.wants
   chsmack -a 'System:Shared' -t %{afm_units_root}/user/default.target.wants
   chsmack -a 'System:Shared' -t %{afm_units_root}/user/sockets.target.wants
   chsmack -a 'System:Shared' -t %{redpeskdir}
   chsmack -a 'System:Shared' -t %{afm_datadir}
   chsmack -a 'System:Shared' -t %{afm_appdir}
   chsmack -a 'System:Shared' -t %{afm_icondir}
fi

%preun
%systemd_preun afm-system-setup.service afm-system-daemon.service afm-system-daemon.socket afmpkg-installer.service afmpkg-installer.socket

%postun
%systemd_postun afm-system-setup.service afm-system-daemon.service afm-system-daemon.socket afmpkg-installer.service afmpkg-installer.socket

%files
%defattr(-,root,root)
%dir %{afm_units_root}/system
%dir %{afm_units_root}/user
%dir %{afm_units_root}/system/multi-user.target.wants
%dir %{afm_units_root}/system/afm-user-session@.target.wants
%dir %{afm_units_root}/user/default.target.wants
%dir %{afm_units_root}/user/sockets.target.wants
%dir %{redpeskdir}
%dir %{afm_datadir}
%dir %{afm_appdir}
%dir %{afm_icondir}
%config %{_sysconfdir}/afm/afm-unit.conf
%config %{_sysconfdir}/afm/certs
%config %{_sysconfdir}/dbus-1/session.d/*
%config %{_sysconfdir}/dbus-1/system.d/*
%config %{_sysconfdir}/pam.d/*
%config %{_presetdir}/%{basename:%{SOURCE1}}
%{_bindir}/*
%{_unitdir}/afm-api-afm-main@.service
%{_unitdir}/afm-system-daemon.service
%{_unitdir}/afm-system-daemon.socket
%{_unitdir}/afmpkg-installer.service
%{_unitdir}/afmpkg-installer.socket
%{_unitdir}/afm-system-setup.service
%{_unitdir}/afm-user-session@.service
%{_unitdir}/afm-user-session@.target
%{_unitdir}/afm-user-setup@.service
%{_unitdir}/user-runtime-dir@.service.wants/afm-user-setup@.service
%{_libexecdir}/afm/afm-system-setup.sh
%{_libexecdir}/afm/afm-create-user.sh
%{_libexecdir}/afm/afm-user-setup.sh
%{_libexecdir}/afm/afm-user-session
%{_libexecdir}/afm/*so
%{afm_units_root}/system/multi-user.target.wants/afm-user-session@%{_rp_owner_id}.service

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/afm-main.pc

%files rpm
%defattr(-,root,root)
%{__plugindir}/redpesk.so
%{_rpmmacrodir}/macros.afm-main

%changelog

* Wed Nov 15 2023 José Bollo jose.bollo@iot.bzh 12.2.0
- Remove patching of pam because legacy, needed before arz-1.1
- Remove installation of macros because now in sources
- Bump to version 12.2.0

* Thu Mar 09 2023 José Bollo jose.bollo@iot.bzh 11.0.1+77+gc534057
Upgrading to 12.0.0

* Fri Jul 23 2021 José Bollo jose.bollo@iot.bzh 10.0.1
- [CI] Create MAINTAINERS file
- Remove requirement to sec-cynagoauth
- Version 10.0.1

* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 10.0.0
- Remove TR_RPMDB that doesn't exists on centos and is useless here
- Fix link order issue
- Version 10.0.0
* Tue Jun 15 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.2
- Upgrade version from source commit sha: db79574b4f8b3ca878a52413fa52a6695bf1d603
- Commit message:
- 	Fix link order issue


* Mon Jun 14 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 10.0.1
- Upgrade version from source commit sha: 0731b47099e89e262ca1d9b3f9c6936a0d025b3e
- Commit message:
- 	Remove TR_RPMDB that doesn't exists on centos and is useless here
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I5ed74c05ced3d9ceac77f89a44dbf41abe4ead6c


* Fri Jun 04 2021 José Bollo jose.bollo@iot.bzh 10.0.0
- wgtpkg-install: Reuse common parts
- wgt-info: Add detection of missing id or version
- wgtpkg-uninstall: Reuse common parts and improve it
- utils-systemd: Improve state helpers
- utils-systemd: Group, sort, align string constants
- utils-systemd: Add method to list units by pattern
- wgtpkg-unit: Add stop of running units on uninstall
- rpm-redpesk: rework install/remove/upgrading rpms
- Allows to remove widgets (replaced by RPM)
- macro.inc: Remove version from UNIT_NAME_BASE
- Version 10.0.0
* Tue May 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.8
- Upgrade version from source commit sha: 9af1383c210d74fa06ed0805f77353bba1cbfd8b
- Commit message:
- 	Version 9.99.8
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I85802ebb4d3634c56c65bdcbdb2472642594f963


* Tue May 25 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.8
- Upgrade version from source commit sha: 8fa81423c3dc7a35803ac67b216f57df150d053c
- Commit message:
- 	setup scripts: correct bug on smack label and uniform script
-
- 	if directory was created label was not correctly set
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I273eea515486ec12ffea8e945de1b185bf697e7c


* Wed May 12 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.7
- Upgrade version from source commit sha: 4691c91a67e8fb03c439ec50bbc8c069f62cc69d
- Commit message:
- 	add chmod and chown on home and app-data directories
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I673b01caeacf4856701e8b686c169f7595658a20


* Thu Apr 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.6
- Upgrade version from source commit sha: c9d4148058d9c707d7810f9ae0c427c0c2cab4cb
- Commit message:
- 	Add cmake option WITH_TOOLS
-
- 	ON by default, this option if set to OFF avoid the generation
- 	of tools wgtpkg-sign wgtpkg-pack wgtpkg-info wgtpkg-install


* Thu Apr 15 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.5
- Upgrade version from source commit sha: aa33a36843d62e04afad29d53a05f14fa02e2f3c
- Commit message:
- 	Add SELinuxContextFromNet=true for socket
-
- 	If this option is not set, we cannot use afb-client
- 	with unix socket. (unconfied_service_t)
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I831313ff1e60819e4da99812c25d1a67ee4c55c9


* Fri Apr 09 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.4
- Upgrade version from source commit sha: 56d9d126fdda8301eb5199c37d94b02370e2a8a9
- Commit message:
- 	Add "-Z" for mkdir in afm-user-setup and afm-system-setup
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I6c19e02500c7d83e17b68ed858ac9b038cfb4f76


* Mon Mar 29 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.3
- Upgrade version from source commit sha: d7ddc2f07b15e029ff2bb1fe95c9956039aa3b86
- Commit message:
- 	rpm-redpesk: add missing line feed on each rpmlog
-
- 	Signed-off-by: Pierre Marzin <pierre.marzin@iot.bzh>


* Wed Mar 24 2021 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.2
- Upgrade version from source commit sha: 0d8e803c860a1a88752670c2ceb4d7f7539352b4
- Commit message:
- 	rpm-redpesk: ignore error uninstall rpm
-
- 	- it prevented from removing packages that was not installed with smack
-
- 	Change-Id: Id3ff702e5f8fcf95f773edeb053fda7e2785c513
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Thu Aug 20 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20200820+16+gdbdc388
- Upgrade version from source commit sha: dbdc388750ec41cc320a2cb007a53f52705d084a
- Commit message:
- 	path type not set
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: I0e5dd23774575598be09c9cf14da96f5130095a3



* Thu Aug 20 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+8+gc0749a7d
- Upgrade version from source commit sha: c0749a7dac99a277669de3add3b5c7be9bbfd0ec
- Commit message:
- 	Use new security-manager
-
- 	The definition of the path type is now :
- 	conf, data, exec, http, icon, id, lib and public
-
- 	By default the choice is made thanks to the name of the directories.
- 	But it is possible to modify them in the configuration file of the widget.
-
- 	/bin/    => exec
- 	/etc/    => conf
- 	/conf/   => conf
- 	/lib/    => lib
- 	/var/    => data
- 	/htdocs/ => http
- 	/public/ => public
-
- 	Signed-off-by: Arthur Guyader <arthur.guyader@iot.bzh>
- 	Change-Id: Ia09bf1c682e142545ce7ba459b680cc16a48da54


* Tue Jun 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+21+g50ebde31
- Upgrade version from source commit sha: 50ebde31cb30b436df756dcf07fbc3c88bbb982d
- Commit message:
- 	rpm-redpesk: handle reinstall process
-
- 	- if reinstall do not uninstall redpesk
-
- 	Change-Id: Ic0e3d8a728c6a2d9e1e667cc63c414a419f5b1b9
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Mon Jun 01 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+20+g2eac4ae1
- Upgrade version from source commit sha: 2eac4ae10a4ea9386acdf5c60632d222bc84c1aa
- Commit message:
- 	wgtpkg-uninstall: uninstall redpesk without icon
-
- 	- based on uninstall widget without icon
-
- 	Change-Id: I0c097c39b685b48123fe790cd1c441c364169517
- 	Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+17+g1a3f1886
- Upgrade version from source commit sha: 1a3f18868b5116ebb6bc5793a63a508076569d8d
- Commit message:
- 	fix rpm-redpesk
-
- 	Change-Id: I30e612a4fe051e5b52848e04ecc3f321ffb6cf25
- 	Signed-off-by: José Bollo <jose.bollo@iot.bzh>


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+16+g707a0e0c
- Upgrade version from source commit sha: 707a0e0c123efa9eb23aaa8378ea041b92f7bd1a
- Commit message:
- 	Merge commit '6e68460' into zzz
-
- 	Change-Id: I19ed649267d2a5348b591f62e941cb1f7c14210b


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> g64e13faa
- Upgrade version from source commit sha: 64e13faaae1110af71042a86a8afca67a2ad087e
- Commit message:
- Merge branch 'rpcle' into zzz
-
- Change-Id: If6226c5787c61fab58f4f6347567d0a8543d731d


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> g64e13faa
- Upgrade version from source commit sha: 64e13faaae1110af71042a86a8afca67a2ad087e
- Commit message:
- Merge branch 'rpcle' into zzz
-
- Change-Id: If6226c5787c61fab58f4f6347567d0a8543d731d


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> g64e13faa
- Upgrade version from source commit sha: 64e13faaae1110af71042a86a8afca67a2ad087e
- Commit message:
- Merge branch 'rpcle' into zzz
-
- Change-Id: If6226c5787c61fab58f4f6347567d0a8543d731d


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.6
- Upgrade version from source commit sha: 64e13faaae1110af71042a86a8afca67a2ad087e
- Commit message:
- Merge branch 'rpcle' into zzz
-
- Change-Id: If6226c5787c61fab58f4f6347567d0a8543d731d


* Wed May 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> g64e13faa
- Upgrade version from source commit sha: 64e13faaae1110af71042a86a8afca67a2ad087e
- Commit message:
- Merge branch 'rpcle' into zzz
-
- Change-Id: If6226c5787c61fab58f4f6347567d0a8543d731d


* Tue May 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+15+gcd0d7297
- Upgrade version from source commit sha: cd0d7297714a1c9fa753f6ddf2877615ee05b133
- Commit message:
- Merge branch 'rpcle' into yyy
-
- Change-Id: Ic51c0c1b03ca6bd6075163660b22cdc1aaf36eb8


* Tue May 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+12+ge7ac3284
- Upgrade version from source commit sha: e7ac328451fa3b3edfbd3658a2365b75d41c0698
- Commit message:
- afm-urun: Fix infinite loop on start status
-
- Ensure that there is no infinite loop when waiting
- for the completion of a status.
-
- Bug-AGL: SPEC-3323
-
- Change-Id: I93537e9bbbe8ef357d112bea1cb6201e96d01ebf
- Signed-off-by: José Bollo <jose.bollo@iot.bzh>


* Tue May 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+12+ge7ac3284
- Upgrade version from source commit sha: e7ac328451fa3b3edfbd3658a2365b75d41c0698
- Commit message:
- afm-urun: Fix infinite loop on start status
-
- Ensure that there is no infinite loop when waiting
- for the completion of a status.
-
- Bug-AGL: SPEC-3323
-
- Change-Id: I93537e9bbbe8ef357d112bea1cb6201e96d01ebf
- Signed-off-by: José Bollo <jose.bollo@iot.bzh>


* Tue May 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+15+gacf09cc7
- Upgrade version from source commit sha: acf09cc72148e0d49bef1a27a1b74d7f48aac86a
- Commit message:
- Merge branch 'rpcle' into xxx
-
- Change-Id: I8a134377400b8b5245a85380f14f447c550292ec


* Wed May 13 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+13+g6e684600
- Upgrade version from source commit sha: 6e6846001d6c97d69501bec9d1270feda63a5bf2
- Commit message:
- rpm-plugin: install widget from directory (no zip)
-
- - instead unzip a widget file: install widget from a directory
-   which is installed by rpm(dnf)
- - rpm-plugin:
-     - install:
- - looking for config.xml file in post psm rpm hook
- - call install_redpesk (similar to install_widget function)
- - sighup afm-system-daemon if proc exists
-     - uninstall:
- - looking for config.xml file in pre psm rpm hook
- - call uninstall_redpesk (similar to uninstall_widget function)
- - sighup afm-system-daemon if proc exists
-
- Change-Id: I73a89f90dfcfaa9fd2272d75261f28eec0a58a3b
- Signed-off-by: Clément Bénier <clement.benier@iot.bzh>


* Sat May 09 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 8.99.5+12+ge7ac3284
- Upgrade version from source commit sha: e7ac328451fa3b3edfbd3658a2365b75d41c0698
- Commit message:
- afm-urun: Fix infinite loop on start status
-
- Ensure that there is no infinite loop when waiting
- for the completion of a status.
-
- Bug-AGL: SPEC-3323
-
- Change-Id: I93537e9bbbe8ef357d112bea1cb6201e96d01ebf
- Signed-off-by: José Bollo <jose.bollo@iot.bzh>


* Sat May 09 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> ge7ac3284
- Upgrade version from source commit sha: e7ac328451fa3b3edfbd3658a2365b75d41c0698
- Commit message:
- afm-urun: Fix infinite loop on start status
-
- Ensure that there is no infinite loop when waiting
- for the completion of a status.
-
- Bug-AGL: SPEC-3323
-
- Change-Id: I93537e9bbbe8ef357d112bea1cb6201e96d01ebf
- Signed-off-by: José Bollo <jose.bollo@iot.bzh>


* Sat May 09 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> ge7ac3284
- Upgrade version from source commit sha: e7ac328451fa3b3edfbd3658a2365b75d41c0698
- Commit message:
- afm-urun: Fix infinite loop on start status
-
- Ensure that there is no infinite loop when waiting
- for the completion of a status.
-
- Bug-AGL: SPEC-3323
-
- Change-Id: I93537e9bbbe8ef357d112bea1cb6201e96d01ebf
- Signed-off-by: José Bollo <jose.bollo@iot.bzh>

* Mon Oct 07 2019 Romain Forlot <romain.forlot@iot.bzh>
- initial creation
