%define url_ver %(echo %{version} | cut -d. -f1,2)

%define api	2.4
%define major	1
%define libname	%mklibname soup- %{api} %{major}
%define girname	%mklibname soup-gir %{api}
%define develname	%mklibname -d soup- %{api} 

%define build_check	0
%define build_doc	0

Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup
Version: 2.38.1
Release: 3
License: LGPLv2
Group: System/Libraries
URL: http://www.gnome.org/
Source0: http://ftp.acc.umu.se/pub/GNOME/sources/libsoup/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
%if %{build_doc}
BuildRequires:	gtk-doc
%endif
%if %{build_check}
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

%package -n %{libname}
Summary:	Libraries for soup
Group:		System/Libraries
Conflicts:	gir-repository < 0.6.5-12.1

%description -n %{libname}
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains libraries used by soup.

%package -n %{girname}
Summary:	GObject Introspection interface library for libsoup
Group:		System/Libraries
Conflicts:	gir-repository < 0.6.5-12.1

%description -n %{girname}
GObject Introspection interface library for libsoup.

%package -n %{develname}
Summary:	Development libraries, header files and utilities for soup
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{develname}
This package contains the files necessary to develop applications with soup.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-tls-check \
%if %{build_check}
	--with-apache-module-dir=/etc/httpd/*modules \
%endif
%if %{build_doc}
	--enable-gtk-doc
%endif

%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -exec rm -rf {} \;

%if %{build_check}
%check
make check
%endif

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Soup-%{api}.typelib
%{_libdir}/girepository-1.0/SoupGNOME-%{api}.typelib

%files -n %{develname}
%doc README COPYING AUTHORS NEWS
%{_datadir}/gtk-doc/html/%{name}-%{api}
%{_datadir}/gir-1.0/Soup-%{api}.gir
%{_datadir}/gir-1.0/SoupGNOME-%{api}.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

