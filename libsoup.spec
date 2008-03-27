%define api_version 2.4
%define lib_major	1
%define lib_name	%mklibname soup- %{api_version} %{lib_major}
%define develname %mklibname -d soup- %{api_version} 

Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup
Version: 2.4.0
Release: %mkrel 2
License: GPL/LGPL
Group: System/Libraries
URL: http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.4.0-2mdv various SVN fixes (HTTP Digest Auth)
Patch0: libsoup-2.4.0-svnfixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: gtk-doc
BuildRequires: libxml2-devel

%description
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

%package -n %{lib_name}
Summary:        Libraries for soup
Group:          System/Libraries

%description -n %{lib_name}
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains libraries used by soup.

%package -n %develname
Summary:        Development libraries, header files and utilities for soup
Group:          Development/GNOME and GTK+
Provides:	%{name}-%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	glib2-devel
Conflicts:	%{_lib}soup-2.2_7-devel
Obsoletes: %mklibname -d soup- 2.2 8

%description -n %develname
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains the files necessary to develop applications with soup.

%prep
%setup -q
%patch0 -p1 -b .svnfixes

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README COPYING AUTHORS NEWS
%{_libdir}/*.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}-%api_version
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


