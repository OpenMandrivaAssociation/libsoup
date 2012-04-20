%define api_version 2.4
%define lib_major	1
%define lib_name	%mklibname soup- %{api_version} %{lib_major}
%define gi_name		%mklibname soup-gir %{api_version}
%define develname	%mklibname -d soup- %{api_version} 

%define build_check		0
%define build_doc		0

Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup
Version: 2.38.1
Release: 1
License: LGPLv2
Group: System/Libraries
URL: http://www.gnome.org/
Source0: http://ftp.acc.umu.se/pub/GNOME/sources/libsoup/2.38/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0) >= 2.27.5
BuildRequires:	pkgconfig(glib-2.0) >= 2.27.5
BuildRequires:	pkgconfig(gobject-2.0) >= 2.27.5
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	gobject-introspection-devel >= 0.9.5
%if %{build_doc}
BuildRequires:	gtk-doc
%endif
%if %build_check
#gw for running checks
BuildRequires:	apache-mod_ssl
BuildRequires:	apache-mod_proxy
BuildRequires:	apache-mod_php
BuildRequires:	php-xmlrpc
%endif
Requires:	glib-networking

%description
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

%package -n %{lib_name}
Summary:	Libraries for soup
Group:		System/Libraries
Conflicts:	gir-repository < 0.6.5-12.1

%description -n %{lib_name}
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains libraries used by soup.

%package -n %{gi_name}
Summary:	GObject Introspection interface library for libsoup
Group:		System/Libraries
Conflicts:	gir-repository < 0.6.5-12.1
Requires:	%{lib_name} = %{version}-%{release}

%description -n %{gi_name}
GObject Introspection interface library for libsoup.

%package -n %{develname}
Summary:	Development libraries, header files and utilities for soup
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}

%description -n %{develname}
This package contains the files necessary to develop applications with soup.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-tls-check \
%if %build_check
	--with-apache-module-dir=/etc/httpd/*modules \
%endif
%if %{build_doc}
	--enable-gtk-doc
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name "*.la" -exec rm -rf {} \;

%if %build_check
%check
make check
%endif

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Soup-%{api_version}.typelib
%{_libdir}/girepository-1.0/SoupGNOME-%{api_version}.typelib

%files -n %{develname}
%doc README COPYING AUTHORS NEWS
%{_datadir}/gtk-doc/html/%{name}-%api_version
%{_datadir}/gir-1.0/Soup-%{api_version}.gir
%{_datadir}/gir-1.0/SoupGNOME-%{api_version}.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


