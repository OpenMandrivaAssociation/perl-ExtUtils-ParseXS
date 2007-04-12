%define	module	ExtUtils-ParseXS
%define	name	perl-%{module}
%define	version	2.16
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Converts Perl XS code into C code 
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-CBuilder
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the constructs
necessary to let C functions manipulate Perl values and creates the glue
necessary to let Perl access those functions.  The compiler uses typemaps to
determine how to map C function parameters and variables to Perl values.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes INSTALL
%{perl_vendorlib}/ExtUtils
%{_mandir}/*/*


