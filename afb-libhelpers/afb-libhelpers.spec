%define debug_package %{nil}

Name: afb-libhelpers
Version: 10.0.0
Release: 6%{?dist}
Summary: Helpers library for AFB
Group:          Development/Libraries/C and C++
License: APL2.0
URL: http://git.ovh.iot/redpesk/redpesk-common/libafb-helpers.git
Source: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: libcurl-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig

%description
libafb-libhelpers is a library to help developping bindings for the AGL application
framework binder. This package include the libraries with support for bindings
using using the API version 3 and version 4. libafb-helpers are for version 3
and libafb-libhelpers for the version 4.

%package devel
Requires:       %{name} = %{version}
Provides:       pkgconfig(%{name}) = %{version}
Summary:  Development headers and library for %{name}

%description devel
libafb-libhelpers devel is a library to help developping bindings for the AGL
application framework binder. This package include the libraries with support
for bindings using using the API version 3 and version 4. libafb-helpers are for
version 3 and libafb-libhelpers for the version 4.

%prep
%autosetup -p 1

%build
%cmake -DCMAKE_BUILD_TYPE=DEBUG .
%if 0%{?fedora} >= 33
%cmake_build
%else
%__make %{?_smp_mflags}
%endif

%install
[ -d build ] && cd build
%if 0%{?fedora} >= 33
%cmake_install
%else
%make_install
%endif
%__ln_s -f %{name}.pc %{buildroot}%{_libdir}/pkgconfig/afb-helpers.pc
%__ln_s -f %{name}-qt.pc %{buildroot}%{_libdir}/pkgconfig/afb-helpers-qt.pc

%check

%clean

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*

%changelog
* Thu Jun 17 2021 José Bollo jose.bollo@iot.bzh 10.0.0
- Update doc
- [DOCS] Remove github users account links
- Remove some unreachable link
- Remove packaging files
- Update doc and remove useless packaging files
- Fix a broken link
- [Doc] Typo Redpesk/redpesk #2025
- Merge divergent branches
- forced timer source to be free
- cleanup
- Upgrade wrap-json and add wrap-base64
- Fix when strncpy doesn't append null
- Version 10.0.0
* Fri Dec 11 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201202+20+g6cc5d85
- Upgrade version from source commit sha: 6cc5d85de9a9f2846c7e2d67cc93814ce785bc30
- Commit message:
- 	Rename also the pkgconfig file to the new name
- 	
- 	Also rename pkgconfig and fix wrong project name
- 	
- 	Change-Id: Id370d7494873dc72332135d92c85fd685f484695
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201202+20+g6cc5d85
- Upgrade version from source commit sha: 6cc5d85de9a9f2846c7e2d67cc93814ce785bc30
- Commit message:
- 	Rename also the pkgconfig file to the new name
- 	
- 	Also rename pkgconfig and fix wrong project name
- 	
- 	Change-Id: Id370d7494873dc72332135d92c85fd685f484695
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201127+18+g4d9c352
- Upgrade version from source commit sha: 4d9c3520b763f4fc3961187dbac9f20125d5bca0
- Commit message:
- 	Follow mass rename of Redpesk packages
- 	
- 	Change-Id: I4686c2e8fb591d54427b7c0944f313e9d12049ac
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201127+18+g4d9c352
- Upgrade version from source commit sha: 4d9c3520b763f4fc3961187dbac9f20125d5bca0
- Commit message:
- 	Follow mass rename of Redpesk packages
- 	
- 	Change-Id: I4686c2e8fb591d54427b7c0944f313e9d12049ac
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201127+18+g4d9c352
- Upgrade version from source commit sha: 4d9c3520b763f4fc3961187dbac9f20125d5bca0
- Commit message:
- 	Follow mass rename of Redpesk packages
- 	
- 	Change-Id: I4686c2e8fb591d54427b7c0944f313e9d12049ac
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Wed Dec 02 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201127+18+g4d9c352
- Upgrade version from source commit sha: 4d9c3520b763f4fc3961187dbac9f20125d5bca0
- Commit message:
- 	Follow mass rename of Redpesk packages
- 	
- 	Change-Id: I4686c2e8fb591d54427b7c0944f313e9d12049ac
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201127+18+g4d9c352
- Upgrade version from source commit sha: 4d9c3520b763f4fc3961187dbac9f20125d5bca0
- Commit message:
- 	Follow mass rename of Redpesk packages
- 	
- 	Change-Id: I4686c2e8fb591d54427b7c0944f313e9d12049ac
- 	Signed-off-by: Romain Forlot <romain.forlot@iot.bzh>


* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201014+15+g78827d9
- Upgrade version from source commit sha: 78827d9195ddabc1b4272d8ce421d1b068182607
- Commit message:
- 	Merge branch 'sb/jobol/fixes' into 'master'
- 	
- 	some fixes
- 	
- 	See merge request redpesk/redpesk-common/libafb-helpers!3


* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201014+15+g78827d9
- Upgrade version from source commit sha: 78827d9195ddabc1b4272d8ce421d1b068182607
- Commit message:
- 	Merge branch 'sb/jobol/fixes' into 'master'
- 	
- 	some fixes
- 	
- 	See merge request redpesk/redpesk-common/libafb-helpers!3


* Fri Nov 27 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201014+15+g78827d9
- Upgrade version from source commit sha: 78827d9195ddabc1b4272d8ce421d1b068182607
- Commit message:
- 	Merge branch 'sb/jobol/fixes' into 'master'
- 	
- 	some fixes
- 	
- 	See merge request redpesk/redpesk-common/libafb-helpers!3


* Mon Oct 19 2020 IoT.bzh(iotpkg) <redpesk.list@iot.bzh> 9.99.1+20201014+15+g78827d9
- Upgrade version from source commit sha: 78827d9195ddabc1b4272d8ce421d1b068182607
- Commit message:
- 	Merge branch 'sb/jobol/fixes' into 'master'
-
- 	some fixes
-
- 	See merge request redpesk/redpesk-common/libafb-libhelpers!3


* Fri May 17 2019 IoT.bzh <silex.list.iot.bzh> 6.99-1
- Creation of the spec file from Silex generator
