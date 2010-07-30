%define api_version 2.4
%define lib_major	1
%define lib_name	%mklibname soup- %{api_version} %{lib_major}
%define develname %mklibname -d soup- %{api_version} 
%define build_check     0
%{?_with_check: %{expand: %%global build_check 1}}

Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup
Version: 2.31.2
Release: %mkrel 3
License: LGPLv2
Group: System/Libraries
URL: http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: libsoup-2.25.5-linking.patch
#gw from git, fix SSL access with gnutls
#http://bugzilla.gnome.org/show_bug.cgi?id=581342
Patch2: libsoup-disable-tls1.2-patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: sqlite3-devel
BuildRequires: libproxy-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libGConf2-devel dbus-glib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: libxml2-devel
%if %build_check
#gw for running checks
BuildRequires: apache-mod_ssl apache-mod_proxy apache-mod_php php-xmlrpc
%endif

%description
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

%package -n %{lib_name}
Summary:        Libraries for soup
Group:          System/Libraries
Conflicts: gir-repository < 0.6.5-12.1

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
#gw .la dep:
Requires:	eggdbus-devel
Conflicts:	%{_lib}soup-2.2_7-devel
Obsoletes: %mklibname -d soup- 2.2 8
Conflicts: gir-repository < 0.6.5-12.1

%description -n %develname
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains the files necessary to develop applications with soup.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
%if %build_check
 --with-apache-module-dir=/etc/httpd/*modules \
%endif
# --enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%if %build_check
%check
make check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README COPYING AUTHORS NEWS
%{_libdir}/*.so.%{lib_major}*
%_libdir/girepository-1.0/Soup-%{api_version}.typelib
%_libdir/girepository-1.0/SoupGNOME-%{api_version}.typelib

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}-%api_version
%_datadir/gir-1.0/Soup-%{api_version}.gir
%_datadir/gir-1.0/SoupGNOME-%{api_version}.gir
#%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


