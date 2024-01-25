%define debug_package %{nil}
ExcludeArch: x86_64

Name: afb-libhelpers
#Hexsha: 15728e63f546b54f8830f15806ab744642f1abdb
Version: 10.0.4+5+g15728e6
Release: 16%{?dist}
Summary: Helpers library for AFB
Group:   Development/Libraries/C and C++
License: Apache-2.0
URL: http://git.ovh.iot/redpesk/redpesk-common/libafb-helpers.git
Source: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(afb-binding)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libsystemd) >= 222
BuildRequires: pkgconfig(librp-utils) >= 0.0.4
BuildRequires: libcurl-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
Requires: libafb-helpers3-static
Requires: libafb-helpers4-static

%description
Metapackage for libafb-libhelpers libraries.

These libraries are to help developping bindings for the AGL application
framework binder. This package include the libraries with support for bindings
using using the API version 3 and version 4.

#------------------------
%package devel
Summary:  Obsolete, link to libafb-helpers3-static
Requires: libafb-helpers3-static

%description devel
This package is here for historical reason and will be removed
in future. It pulls the real package whose name is libafb-helpers3-static.

#------------------------
%package -n libafb-helpers3-static
Summary:   Development headers and library for %{name} version 3
Provides:  pkgconfig(afb-libhelpers) = %{version}
Provides:  pkgconfig(afb-helpers3) = %{version}
Provides:  pkgconfig(afb-helpers) = %{version}
Provides:  afb-libhelpers-devel = %{version}

%description -n libafb-helpers3-static
libafb-libhelpers devel is a library to help developping bindings for the AGL
application framework binder. This package include the libraries with support
for bindings using using the API version 3.

#------------------------
%package -n libafb-helpers4
Summary: Libraries for libafb-helpers version 4

%description  -n libafb-helpers4
Shared libraries for libafb-helpers4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%package -n afb-helpers4-headers
Summary: Header files for library for libafb-helpers version 4

%description  -n afb-helpers4-headers
Header files for library for libafb-helpers4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%package -n afb-helpers4-devel
Summary:   Development files for library for libafb-helpers version 4
Requires:  libafb-helpers4 = %{version}
Requires:  afb-helpers4-headers = %{version}
Provides:  pkgconfig(afb-helpers4) = %{version}

%description  -n afb-helpers4-devel
Development files for library for libafb-helpers4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%package -n afb-helpers4-static
Summary:    Static library for libafb-helpers version 4
Requires:   afb-helpers4-headers = %{version}
Provides:   pkgconfig(afb-helpers4-static) = %{version}

%description -n afb-helpers4-static
Static library for afb-helpers4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%package -n libafb-helpers++4
Summary:   Libraries for libafb-helpers++ version 4
Requires:  libafb-helpers4 >= %{version}

%description  -n libafb-helpers++4
Shared libraries for afb-helpers++4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%package -n afb-helpers++4-devel
Summary:   Development files for library for libafb-helpers++ version 4
Requires:  libafb-helpers++4 >= %{version}
Requires:  afb-helpers4-devel >= %{version}
Provides:  pkgconfig(afb-helpers++4) = %{version}

%description  -n afb-helpers++4-devel
Development files for library for libafb-helpers++4.

The libraries libafb-libhelpers are intended to provide helper
functions for C developpers of afb-bindings.

#------------------------
%prep
%autosetup -p 1

%build
%cmake -DCMAKE_BUILD_TYPE=DEBUG .
%cmake_build

%install
%cmake_install

%check

%clean

%post -n libafb-helpers4
/sbin/ldconfig

%postun -n libafb-helpers4
/sbin/ldconfig

%post -n libafb-helpers++4
/sbin/ldconfig

%postun -n libafb-helpers++4
/sbin/ldconfig

%files

%files devel

%files -n libafb-helpers3-static
%{_libdir}/libafb-helpers3.a
%{_libdir}/pkgconfig/afb-helpers3.pc
%{_libdir}/pkgconfig/afb-helpers.pc
%{_libdir}/pkgconfig/afb-libhelpers.pc
%dir %{_includedir}/afb-helpers/
%{_includedir}/afb-helpers/*

%files -n libafb-helpers4
%{_libdir}/libafb-helpers4.so.*

%files -n afb-helpers4-headers
%dir %{_includedir}/afb-helpers4/
%{_includedir}/afb-helpers4/*.h

%files -n afb-helpers4-devel
%{_libdir}/libafb-helpers4.so
%{_libdir}/pkgconfig/afb-helpers4.pc

%files -n afb-helpers4-static
%{_libdir}/libafb-helpers4.a
%{_libdir}/pkgconfig/afb-helpers4-static.pc

%files -n libafb-helpers++4
%{_libdir}/libafb-helpers++4.so.*

%files -n afb-helpers++4-devel
%{_libdir}/libafb-helpers++4.so
%{_libdir}/pkgconfig/afb-helpers++4.pc
%{_includedir}/afb-helpers4/*.hpp
%{_includedir}/afb-helpers4/afb-data-utils

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
