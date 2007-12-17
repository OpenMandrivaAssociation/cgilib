%define	major 0
%define libname	%mklibname cgi %{major}

Summary:	A CGI (Common Gateway Interface) library
Name:		cgilib
Version:	0.5
Release:	%mkrel 5
License:	GPL
Group:		System/Libraries
URL:		http://www.infodrom.org/projects/cgilib/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-debian.patch
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool

%description
This is quite a simple library that provides an easy CGI interface (Common
Gateway Interface). It provides an easy to use interface to CGI if you need
to write your program in C instead of perl.

%package -n	%{libname}
Summary:	A CGI (Common Gateway Interface) library
Group:          System/Libraries
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{libname}
This is quite a simple library that provides an easy CGI interface (Common
Gateway Interface). It provides an easy to use interface to CGI if you need
to write your program in C instead of perl.


%package -n	%{libname}-devel
Summary:	Development library and header files for the %{libname} library
Group:		Development/C
Obsoletes:	%{name}-devel
Provides:	%{name}-devel
Provides:	libcgi-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
Header files and develpment documentation for %{name}.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} -fPIC"
touch NEWS README AUTHORS ChangeLog
libtoolize --copy --force; aclocal-1.7; autoconf; automake-1.7 --add-missing --copy

%configure2_5x

%make CFLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES CREDITS readme
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_mandir}/man[35]/*


