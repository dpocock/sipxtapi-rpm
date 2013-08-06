Name: sipxtapi
Version: 3.3.0~test11
Release: 1

Summary: SIP stack, RTP media framework and codecs
License: LGPL
Group: Development/Libraries
Vendor: SIPfoundry
Packager: Daniel Pocock <daniel@pocock.com.au>
Url: http://sipxtapi.sipfoundry.org

Source: %name-%version.tar.gz

BuildRequires: libtool automake autoconf
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: gsm-devel
BuildRequires: openssl-devel >= 0.9.8
BuildRequires: pcre-devel
BuildRequires: spandsp-devel
BuildRequires: xerces-c-devel
Requires: openssl >= 0.9.8

%description
sipXtapi is a framework that makes it easy to construct SIP user agents,
including softphones and telephony servers.

%package libs
Summary: Shared libraries http://sipxtapi.sipfoundry.org

%description libs
sipXtapi is a framework that makes it easy to construct SIP user agents,
including softphones and telephony servers.

This package provides the libraries for dynamic linking.

%package devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Group: Development/Libraries
Vendor: SIPfoundry
Summary: Header files for %name

%description devel
sipXtapi is a framework that makes it easy to construct SIP user agents,
including softphones and telephony servers.

This package provides headers and resources for development.

%package apidoc
Group: Development/Libraries
Vendor: SIPfoundry
Summary: API documentation for %name

%description apidoc
sipXtapi is a framework that makes it easy to construct SIP user agents,
including softphones and telephony servers.

This package provides developer documentation about the API.

%prep
%setup -q

%build
%configure --enable-topology-graph --disable-codec-ilbc --disable-codec-g726 --enable-codec-g722 --enable-codec-gsm
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.a
rm -f %{buildroot}%{_libdir}/lib*.la
rm -rf %{buildroot}%{_bindir}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files libs
%doc COPYING
%{_libdir}/lib*.so.*
%{_libdir}/sipxtapi/

%files devel
%{_includedir}/sipxtapi/
%{_libdir}/lib*.so
%{_datarootdir}

%files apidoc
%{_docdir}

%changelog
* Mon May  6 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test11-1
- Initial build

