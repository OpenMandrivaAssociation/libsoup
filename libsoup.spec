%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2.4
%define major	1
%define libname %mklibname soup %{api} %{major}
%define libgnome %mklibname soup-gnome %{api} %{major}
%define girname %mklibname soup-gir %{api}
%define girgnome %mklibname soupgnome-gir %{api}
%define devname %mklibname -d soup %{api} 

%define build_check 0
%define build_doc 0

Summary:	SOAP (Simple Object Access Protocol) implementation
Name:		libsoup
Version:	2.44.2
Release:	4
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libsoup/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0) >= 2.27.5
BuildRequires:	pkgconfig(glib-2.0) >= 2.27.5
BuildRequires:	pkgconfig(gobject-2.0) >= 2.27.5
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
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

%package -n %{libname}
Summary:	Libraries for soup
Group:		System/Libraries
Obsoletes:	%{_lib}soup-2.4_1 < 2.43.1-2

%description -n %{libname}
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains a library used by soup.

%package -n %{libgnome}
Summary:	Libraries for soup
Group:		System/Libraries
Conflicts:	%{_lib}soup-2.4_1 < 2.43.1-2

%description -n %{libgnome}
This package contains a library used by soup.

%package -n %{girname}
Summary:	GObject Introspection interface library for libsoup
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for libsoup.

%package -n %{girgnome}
Summary:	GObject Introspection interface library for libsoup
Group:		System/Libraries
Conflicts:	%{_lib}soup-gir2.4 < 2.43.1-2

%description -n %{girgnome}
GObject Introspection interface library for libsoup.

%package -n %{devname}
Summary:	Development libraries, header files and utilities for soup
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgnome} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girgnome} = %{version}-%{release}
Obsoletes:	%{_lib}soup-2.4-devel < 2.43.1-2

%description -n %{devname}
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
%makeinstall_std
%find_lang %{name}

%if %{build_check}
%check
make check
%endif

%files -n %{libname} -f %{name}.lang
%{_libdir}/libsoup-%{api}.so.%{major}*

%files -n %{libgnome}
%{_libdir}/libsoup-gnome-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Soup-%{api}.typelib

%files -n %{girgnome}
%{_libdir}/girepository-1.0/SoupGNOME-%{api}.typelib

%files -n %{devname}
%doc README COPYING AUTHORS NEWS
%{_datadir}/gtk-doc/html/%{name}-%api
%{_datadir}/gir-1.0/Soup-%{api}.gir
%{_datadir}/gir-1.0/SoupGNOME-%{api}.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

