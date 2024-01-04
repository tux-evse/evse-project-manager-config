#---------------------------------------------
# spec file for package afb-libafb
#---------------------------------------------

Name:           afb-libafb
#Hexsha: cb33a556098f99dea3ed1ed351a6fdd023ba9651
Version:        5.0.9
Release: 	44%{?dist}
License:        GPL-3.0-only
Summary:        Library of internals of application framework binder
Group:          Development/Libraries/C and C++
Url:            https://github.com/redpesk-core/afb-libafb
Source:         %{name}-%{version}.tar.gz
Buildroot:      afb-libafb

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.60
BuildRequires:  pkgconfig(libsystemd) >= 222
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(afb-binding) >= 4.1.2
BuildRequires:  pkgconfig(librp-utils) >= 0.0.4
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  file-devel
%if 0%{?redpesk_ver}
BuildRequires:  pkgconfig(cynagora)
%endif


%description
Library of internals for the application framework binder,
its derivates and its clients.

#---------------------------------------------
%package -n libafb5
Group:          Development/Libraries/C and C++
Summary:        Application Framework Binder core library

%description -n libafb5
Application Framework Binder core library

#---------------------------------------------
%package -n libafb-headers
Group:          Development/Libraries/C and C++
Summary:        Header files for application Framework Binder core library

%description -n libafb-headers
Header files for application Framework Binder core library

#---------------------------------------------
%package -n libafb-devel
Group:          Development/Libraries/C and C++
Requires:       libafb5 = %{version}
Requires:       libafb-headers = %{version}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(afb-binding)
Provides:       pkgconfig(libafb) = %{version}
Summary:        Development files for application Framework Binder core shared library

%description -n libafb-devel
Development files for application Framework Binder core shared library

#---------------------------------------------
%package -n libafb-static
Group:          Development/Libraries/C and C++
Requires:       libafb-headers = %{version}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(afb-binding)
Summary:        Development files for application Framework Binder core static library

%description -n libafb-static
Development files for application Framework Binder core static library

#---------------------------------------------
%package -n libafbcli5
Group:          Development/Libraries/C and C++
Summary:        Application Framework Binder client library

%description -n libafbcli5
Application Framework Binder client library

#---------------------------------------------
%package -n libafbcli-headers
Group:          Development/Libraries/C and C++
Summary:        Header files for application Framework Binder client library

%description -n libafbcli-headers
Header files for application Framework Binder client library

#---------------------------------------------
%package -n libafbcli-devel
Group:          Development/Libraries/C and C++
Requires:       libafbcli5 = %{version}
Requires:       libafbcli-headers = %{version}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(libsystemd) >= 222
Provides:       pkgconfig(libafbcli) = %{version}
Summary:        Development files for application Framework Binder client library shared

%description -n libafbcli-devel
Development files for application Framework Binder client library shared

#---------------------------------------------
%package -n libafbcli-static
Group:          Development/Libraries/C and C++
Requires:       libafbcli-headers = %{version}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(libsystemd) >= 222
Summary:        Development files for application Framework Binder client library static

%description -n libafbcli-static
Development files for application Framework Binder client library static

#---------------------------------------------
%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
CFLAGS="${CFLAGS:-%optflags} -ffat-lto-objects"
%if 0%{?redpesk_ver}
%define without_cynagora OFF
%else
%define without_cynagora ON
%endif
%cmake -DWITH_LIBUUID=OFF -DWITHOUT_CYNAGORA=%{without_cynagora} -DWITH_GNUTLS=ON .
%cmake_build

%install
%cmake_install

#---------------------------------------------
%post -n libafb5
/sbin/ldconfig

%postun -n libafb5
/sbin/ldconfig

%files -n libafb5
%defattr(-,root,root)
%{_libdir}/libafb.so.*

#---------------------------------------------
%files -n libafb-headers
%defattr(-,root,root)
%dir %{_includedir}/libafb
%{_includedir}/libafb/*

#---------------------------------------------
%files -n libafb-devel
%defattr(-,root,root)
%{_libdir}/libafb.so
%{_libdir}/pkgconfig/libafb.pc

#---------------------------------------------
%files -n libafb-static
%defattr(-,root,root)
%{_libdir}/libafb.a

#---------------------------------------------
%post -n libafbcli5
/sbin/ldconfig

%postun -n libafbcli5
/sbin/ldconfig

%files -n libafbcli5
%defattr(-,root,root)
%{_libdir}/libafbcli.so.*

#---------------------------------------------
%files -n libafbcli-headers
%defattr(-,root,root)
%dir %{_includedir}/libafbcli
%{_includedir}/libafbcli/*

#---------------------------------------------
%files -n libafbcli-devel
%defattr(-,root,root)
%{_libdir}/libafbcli.so
%{_libdir}/pkgconfig/libafbcli.pc

#---------------------------------------------
%files -n libafbcli-static
%defattr(-,root,root)
%{_libdir}/libafbcli.a

#---------------------------------------------
%changelog

* Tue Jan 5 2023 José Bollo jose.bollo@iot.bzh 5.0.0
- refactor packaging
- switch to v5.0

* Thu Dec 16 2021 José Bollo jose.bollo@iot.bzh 4.0.4+23+g6580d62
- core/apiset: Add function afb_apiset_subset_find
- json-locator: Don't use deprecated functions
- Prepare version 4.1.0
- afb-extend: Improve interface
- libafb-config: Fix macro for handling versions
- ev-mgr: Fix issue on timers
- ev-mgr: Add function ev_mgr_prepare_with_wakeup
- afb-jobs: Add fonction to dequeue multiple jobs
- x-cond: Add function for timedwait
- x-thread: Add functions
- x-errno: Add X_ETIMEDOUT
- afb-threads: Add basic thread manager
- afb-evt: Full rewrite of the SCHEDULER
- afb-api-v4: Fixes and improvements
- Drop legacy code
- afb-threads: improve debugging output
- afb-threads: Add a reserve of started threads
- Remove unnecessary code
- afb-threads: Integration as a core component
- afb-jobs: Add compile option WITH_JOB_NOT_MONITORED
- afb-ev-mgr: Add support for getting the event loop
- afb-sched: Remove management of event loop
- afb-sched: Improve exit status of afb_sched_start

* Fri Nov 19 2021 José Bollo jose.bollo@iot.bzh 4.0.4
- [CI] Create MAINTAINERS file
- json-locator: Fixes
- json-locator: More fixes
- afb-wsj1: Improve msg_scan reports
- afb-wsj1: Pass size of the array as a parameter
- afb-wsj1: Avoid freeing text in message building
- afb-wsj1: Explicit error message when closing
- afb-stub-ws: Minor rename and add comments
- afb-stub-ws: Remove unused structure
- afb-error-text: Add function afb_error_code
- afb-type: Fix initialization of flag
- afb-type: Fix detection of overflow
- afb-type: Add typeid and predefined typeids
- afb-api-rpc: First integration of RPC version 2
- afb-stub-rpc: Fix reference count in v1
- afb-api-rpc: Allows websocket for RPC
- afb-api-rpc: Handle credentials of clients
- afb-rpc-v1: Fix read issues
- afb-api-rpc: Add unpacking messages on option
- afb-hreq: Return binary blobs as HTTP content
- Prepare version 4.0.4
- afb-hreq: Split req_reply in two
- afb-hreq: Fix memory leak
- afb-hsrv: Enforce no concurrent call to MHD_run
- afb-hreq: Fix a warning
- afb-type-predefined: stringz aren't bytearrays
- afb-type: Improve conversion to family member
- Enforce requiring afb-binding >= 4.0.3
- Prepare specialized interfaces for requests
- afb-req-common: Add function for getting interface
- afb-hreq: Implement req_http_x4 itf
- Fix white spaces
- afb-rpc: Add afb-rpc basic tests
- afb-socket: Introduce char type with prefix char:
- afb-api-rpc: Adaptation to handle char devices
- afb-stub-rpc: Fix compatibility to old json-c
- protocols: Add protocol specifications
- afb-sched: Fix use before init (in debug only)
- afb-cred: Enforce use of default credentials
- afb-trace: Fix bug in in tracing
- Fix automatic pong implementation
- afb-sched: REWORK SCHEDULING
- Version 4.0.4

* Thu Jul 01 2021 José Bollo jose.bollo@iot.bzh 4.0.3
- Improve versions for pkgconfig
- afb-api-v4: add functions for event handling
- Improve comments
- afb-req-common: Add setter for parameters
- afb-hreq: Fix POST/HTTP requests
- Version 4.0.3

* Wed Jun 16 2021 Jose Bollo jose.bollo@iot.bzh 4.0.2
- afb-hreq: Save bytes for keys of data
- afb-hreq: Avoid alloc/free for session cookies
- afb-hreq: Add tracking of second HTTP response
- afb-json-legacy: Cleaner interface for making strings
- afb-json-legacy: returns the status code
- Add changlog file
- afb-extension: Enforce string to define extensions
- afb-v4-itf: Check revision of the interface
- afb-type-predefined: Always include basic types
- afb-req-common: Touch the session
- wrap-base64: Isolate base64 functions
- wrap-base64: Add a zero at the end of decoded buffer
- afb-hreq: Remove cookie's attribute 'Secure'
- afb-type-predefined: Split helper functions
- afb-type-predefined: Review exporting of aliases
- afb-type-predefined: Comment of macros
- afb-type-predefined: Add afb_type_predefined_bytearray
- afb-req-common: Tiny renaming
- afb-req-common: Allow tuning size of 'asyncitems'
- afb-json-legacy: Use one-way variables in struct mkmsg
- afb-req-common: Make errors efficient for version 4
- wrap-base64: Fix a spurious warning
- afb-data: Allow allocate uninitialized memory
- afb-req-common: Ensure 'clean_args' can be called twice
- afb-type: Handle more than one converter
- afb-api-v[34]: Allow same address in main callbacks
- Update changelog
- afb-req-common: Implement conversion of parameters
- ev-mgr: Ensure early setting of event listeners
- test-afb-data: Fix uninitialized variable
- afb-extend: Allow interface V4 in extensions
- Version 4.0.2
* Tue Apr 13 2021 José Bollo jose.bollo@iot.bzh 4.0.1

* Fri Apr 09 2021 José Bollo jose.bollo@iot.bzh 4.0.0
- afb-v4: Fix of various glitches
- Improve includes of afb-v4.h and afb-extension.h
- x-dynlib: Add source file for dynamic libraries
- afb-data: Ensure by reading that NULL is set on convert error
- afb-api-v4: Fix mainctl not in description
- afb-hsrv: Add locale in alias names (readability)
- afb-hreq: Refactor replying file
- afb-hsrv: Add aliasing to weak directories
- afb-json-legacy: Fix bug of legacy tagging
- afb-data: Minor reorder of functions
- afb-data: Isolate changed data
- afb-ws-client: Fix libafbcli for serving
- afb-hsrv: Fix new alias to directories
- mkbuild: Allow build every where
- Version 4.0.0

* Thu Mar 25 2021 José Bollo jose.bollo@iot.bzh 4.0.0.beta14
- afb-data: Improve naming
- Update README.md
- Check headers for making it "stand-alone"
- Fix installation of afb-extension.h and remove afb-legacy.h
- afb-v4: Add header for unified naming
- afb-type: Add afb_type_lookup function
- core/afb-v4 -> core/afb-v4-itf to avoid confusions
- afb-data: Add helpers
- afb-data: Prepare unified namings
- afb-param -> afb-data-array for unification of names
- Add functions for unification
- afb-v4: Add function renames
- afb-hreq: Fix cookie setting to Lax+Secure
- afb-req-v[34]: Add functions to get the req_common
- afb-session: Set the timeout
- afb-session: Improve documentation
- Refactor the cookies to allow specific free closure
- afb-global: Add a global api
- afb-data: Makes newly created data mutable
- Version 4.0.0.beta13
- tls: Fix starvation on read
- Version 4.0.0.beta14

* Mon Mar 15 2021 José Bollo jose.bollo@iot.bzh 4.0.0.beta12
- Minor fixes revealed by code analysis
- Replace usleep with nanosleep
- afb-hsrv: Allows NULL for basepath
- Fix cmake version to be ubuntu 18.04 compatible
- afb-hreq: Add SameSite=Strict when setting cookies
- afb-ws-client: add include <time.h> for nanosleep
- Version 4.0.0.beta12
- Add high level headers

* Tue Jan 26 2021 José Bollo <jose.bollo@iot.bzh> 4.0.0beta7
- Use gnuTLS
- Fix redirect of aliases

* Thu Jan 7 2021 José Bollo <jose.bollo@iot.bzh> 4.0.0beta6
- Raise disconnected event on request
- Allow json in info strings of verbs and apis
- Fix HTTP lacking of Preferred-Language
- Update copyright notices

* Thu Dec 17 2020 José Bollo <jose.bollo@iot.bzh> 4.0.0beta5
- Fix deadlock

* Mon Dec 14 2020 José Bollo <jose.bollo@iot.bzh> 4.0.0beta4
- Direct processing of HTTP events
- Fix use of cmake

* Fri Dec 11 2020 José Bollo <jose.bollo@iot.bzh> 4.0.0beta3
- Add delaying of jobs API v3
- Fix name of monitoring events
- Ensure null length of NULL stringz
- Avoid SEGV if NULL string

* Thu Dec 10 2020 José Bollo <jose.bollo@iot.bzh> 4.0.0beta3
- listing of apis
- getting LOA
- remove depend of pc files

