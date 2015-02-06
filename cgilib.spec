%define	major 1
%define libname %mklibname cgi %{major}
%define develname %mklibname cgi -d

Summary:	A CGI (Common Gateway Interface) library
Name:		cgilib
Version:	0.7
Release:	4
License:	GPL
Group:		System/Libraries
URL:		http://www.infodrom.org/projects/cgilib/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
This is quite a simple library that provides an easy CGI interface (Common
Gateway Interface). It provides an easy to use interface to CGI if you need
to write your program in C instead of perl.

%package -n	%{libname}
Summary:	A CGI (Common Gateway Interface) library
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name}

%description -n	%{libname}
This is quite a simple library that provides an easy CGI interface (Common
Gateway Interface). It provides an easy to use interface to CGI if you need
to write your program in C instead of perl.

%package -n	%{develname}
Summary:	Development library and header files for the %{libname} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel
Provides:	libcgi-devel
Obsoletes:	%{mklibname cgi 0 -d}

%description -n	%{develname}
Header files and develpment documentation for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
touch NEWS README AUTHORS ChangeLog
autoreconf -if
%configure2_5x

%make CFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std

# remove unwanted files
rm -f %{buildroot}%{_bindir}/{cgitest,jumpto}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/libcgi.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man[35]/*


%changelog
* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2010.0
+ Revision: 413227
- rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.7-1mdv2009.1
+ Revision: 360125
- Updated to version 0.7
- Dropped merged/obsolete patch: cgilib-ac_am.diff

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdv2009.1
+ Revision: 316501
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2009.0
+ Revision: 264348
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdv2009.0
+ Revision: 200695
- 0.6
- rediff P0
- drop P1, it's in there
- fix devel naming

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5-5mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-5mdv2007.0
+ Revision: 134418
- Import cgilib

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5-5mdv2007.1
- use the %%mkrel macro

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.5-4mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.5-3mdk
- Rebuild

* Thu May 12 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-2mdk
- rebuild
- rpmlint fixes

* Tue Jun 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial PLD import (though a lot mkdified)

