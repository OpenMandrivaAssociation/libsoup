%define api_version 2.4
%define lib_major	1
%define lib_name	%mklibname soup- %{api_version} %{lib_major}
%define gi_name		%mklibname soup-gir %{api_version}
%define develname	%mklibname -d soup- %{api_version} 

%define build_check		0
%define build_doc		0

Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup
Version: 2.40.0
Release: 1
License: LGPLv2
Group: System/Libraries
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/libsoup/2.40/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0) >= 2.27.5
BuildRequires:	pkgconfig(glib-2.0) >= 2.27.5
BuildRequires:	pkgconfig(gobject-2.0) >= 2.27.5
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	intltool
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

%find_lang %{name}

%if %build_check
%check
make check
%endif

%files -n %{lib_name} -f %{name}.lang
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


%changelog
* Tue Oct  9 2012 Arkady L. Shane <ashejn@rosalab.ru. 2.40.0-1
- update to 2.40.0

* Fri Apr 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.38.1-1
+ Revision: 792479
- version update 2.38.1

* Thu Nov 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.36.1-1
+ Revision: 731418
- new version 2.36.1
- cleaned up spec
- removed .la files
- split out gi pkg (mga)
- added build_doc option
- removed mkrel
- removed defattr
- removed old ldconfig scriptlets
- disabled static build
- removed extra devel pkg virtual provide
- converted BRs to pkgconfig provides
- removed BuildRoot
- removed reqs for devel pkgs in devel pkg
- removed clean section
- converted RPM_BUILD_ROOT to buildroot

* Fri Jul 29 2011 Götz Waschk <waschk@mandriva.org> 2.34.3-1
+ Revision: 692230
- new version
- xz tarball

* Mon May 23 2011 Götz Waschk <waschk@mandriva.org> 2.34.2-1
+ Revision: 677966
- update to new version 2.34.2

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 2.34.1-1
+ Revision: 659089
- update to new version 2.34.1

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 2.34.0-2
+ Revision: 650853
- drop unused br

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 2.34.0-1
+ Revision: 650437
- fix br

  + Götz Waschk <waschk@mandriva.org>
    - depend on glib-networking
    - new version
    - drop patch

* Tue Nov 30 2010 Götz Waschk <waschk@mandriva.org> 2.32.2-1mdv2011.0
+ Revision: 603404
- update to new version 2.32.2

* Tue Nov 16 2010 Götz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597925
- update to new version 2.32.1

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581640
- update to new version 2.32.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578094
- new version
- drop patch 1

* Sat Sep 11 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-3mdv2011.0
+ Revision: 577207
- fix build with new gobject-introspection

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570966
- update to new version 2.31.90

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-2mdv2011.0
+ Revision: 568147
- rebuild for new libproxy

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565373
- new version
- drop patch 2

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.2-3mdv2011.0
+ Revision: 563373
- new version
- add introspection support
- conflict with older gir-repository

* Mon Jul 12 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-2mdv2011.0
+ Revision: 551231
- fix ssl access
- add support for running the testsuite

* Wed Jun 23 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2-1mdv2010.1
+ Revision: 548660
- Release 2.30.2

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.30.1-2mdv2010.1
+ Revision: 540357
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539445
- update to new version 2.30.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528930
- update to new version 2.30.0

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.29.91-1mdv2010.1
+ Revision: 509947
- update to new version 2.29.91

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502603
- update to new version 2.29.90

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496492
- update to new version 2.29.6

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-2mdv2010.1
+ Revision: 490631
- update devel deps

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 490412
- update to new version 2.29.5

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 2.29.3-2mdv2010.1
+ Revision: 481473
- fix gir build
- disable gtk-doc

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475430
- update to new version 2.29.3

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458836
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446842
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437459
- update to new version 2.27.92

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420749
- update build deps
- update to new version 2.27.91

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414479
- new version
- drop patch 1

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-2mdv2010.0
+ Revision: 410236
- fix warnings caused by libsoup headers

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 401408
- update to new version 2.27.5

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395473
- update to new version 2.27.4

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 386467
- update to new version 2.27.2

* Thu May 07 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.27.1-1mdv2010.0
+ Revision: 373066
- Updated to 2.27.1

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366931
- update to new version 2.26.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356172
- update build deps
- update to new version 2.26.0

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341276
- update to new version 2.25.91

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 336734
- new version
- fix build
- depend on libproxy

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 325243
- update to new version 2.25.4

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 315882
- drop patch
- fix build deps
- update to new version 2.25.3

* Tue Dec 02 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 309055
- update to new version 2.25.2

* Wed Nov 05 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299990
- fix build deps again
- fix build deps
- new version
- fix linking

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295933
- update to new version 2.24.1

* Wed Sep 24 2008 Götz Waschk <waschk@mandriva.org> 2.24.0.1-1mdv2009.0
+ Revision: 287806
- new version

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286843
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282824
- new version

* Tue Sep 02 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 278807
- new version

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 263340
- new version
- drop patch

* Fri Jul 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.1-1mdv2009.0
+ Revision: 231605
- new version
- update license
- patch to make it build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2009.0
+ Revision: 192469
- new version
- drop patch

* Thu Mar 27 2008 Frederic Crozat <fcrozat@mandriva.com> 2.4.0-2mdv2008.1
+ Revision: 190737
- Patch0 : various fixes from SVN (including HTTP Digest Authentication)

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2008.1
+ Revision: 183693
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.3.4-1mdv2008.1
+ Revision: 175037
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.3.2-1mdv2008.1
+ Revision: 165689
- new version
- new major
- update file list

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.3.0.1-1mdv2008.1
+ Revision: 159519
- new version
- update file list

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2008.1
+ Revision: 159381
- new version
- new api
- new major

* Thu Jan 17 2008 Thierry Vignaud <tv@mandriva.org> 2.2.104-2mdv2008.1
+ Revision: 154149
- do not package big changelog
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Nov 27 2007 Götz Waschk <waschk@mandriva.org> 2.2.104-1mdv2008.1
+ Revision: 113314
- new version

* Sun Oct 28 2007 Götz Waschk <waschk@mandriva.org> 2.2.103-1mdv2008.1
+ Revision: 102868
- new version

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 2.2.102-1mdv2008.1
+ Revision: 98531
- new version

* Wed Oct 10 2007 Götz Waschk <waschk@mandriva.org> 2.2.101-2mdv2008.1
+ Revision: 96656
- fix obsoletes

* Sat Oct 06 2007 Götz Waschk <waschk@mandriva.org> 2.2.101-1mdv2008.1
+ Revision: 95654
- new version
- new devel name

