%define	major 1
%define libname %mklibname cgi %{major}
%define develname %mklibname cgi -d

Summary:	A CGI (Common Gateway Interface) library
Name:		cgilib
Version:	0.7
Release:	%mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.infodrom.org/projects/cgilib/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# remove unwanted files
rm -f %{buildroot}%{_bindir}/{cgitest,jumpto}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/libcgi.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_mandir}/man[35]/*
