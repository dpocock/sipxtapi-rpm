Name:           sipxtapi
Version:        3.3.0~test12
Release:        6%{?dist}
Summary:        SIP stack, RTP media framework and codecs
# LGPLv2 is used for the bulk of the code and is the most restrictive
# license.
# Some examples include code that is licensed under the GPL or Mozilla
# license terms.  As these are examples they are not compiled or
# distributed in the binary package and do not have any impact on
# the licensing of the sipXtapi libraries or any products depending
# on sipXtapi libraries.
# Some codec plugins depend on spandsp, an LGPLv2 licensed library with
# some GPL sample code. Comments in the sipxtapi source code
# (MpStaticCodecInit.h) refer to the GPL components of spandsp.
# The code itself uses the LGPLv2 spandsp package from Fedora.
# As plugins are optional and they are dynamically linked on demand
# at runtime, they do not undermine the LGPLv2 licensing of the sipxtapi
# library itself.
# Some build system artifacts are GPL licensed.  These artifacts are
# not part of the binary package.
# Some individual source files are marked with a BSD-style license
# The wording of these licenses varies slightly from one author
# to the next but the terms are clearly BSD
# Individual authors are named in source files
License:        LGPLv2
Url:            http://www.sipxtapi.org
Source0:        http://download.sipxtapi.org/files/pub/sipX/%{name}-%{version}.tar.gz

BuildRequires:  libtool automake autoconf
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  gsm-devel
BuildRequires:  openssl-devel >= 0.9.8
BuildRequires:  pcre-devel
BuildRequires:  spandsp-devel

%description
sipXtapi is a framework that makes it easy to construct SIP user agents,
including soft-phones and telephony servers.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Development files for %{name}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: API documentation for %{name}

%description doc
sipXtapi is a framework that makes it easy to construct SIP user agents,
including softphones and telephony servers.

This package provides developer documentation about the API.

%prep
%setup -q

%build
%configure --enable-topology-graph --disable-codec-ilbc --disable-codec-g726 --enable-codec-g722 --enable-codec-gsm --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

# sipXtapi provides unit tests but they are not currently invoked
# automatically as they demand network access and other local resources
# that have to be manually configured
#%%check

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/lib*.a
rm -f %{buildroot}%{_libdir}/lib*.la
rm -f %{buildroot}%{_libdir}/%{name}/codecs/codec_*.la
rm -rf %{buildroot}%{_bindir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/lib*.so.*
%{_libdir}/sipxtapi/

%files devel
%{_includedir}/sipxtapi/
%{_libdir}/lib*.so
%{_datadir}/sipxtapi/

%files doc
%doc %{_docdir}/%{name}/*
%{_docdir}/%{name}/

%changelog
* Thu Aug  8 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test12-6
- More fixes

* Thu Aug  8 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test12-5
- New tarball, fix download URL

* Wed Aug  7 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test11-4
- Tweak documentation packaging

* Wed Aug  7 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test11-3
- Various spec file improvements

* Wed Aug  7 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test11-2
- Various spec file improvements

* Mon May  6 2013 Daniel Pocock <daniel@pocock.com.au> - 3.3.0~test11-1
- Initial build
