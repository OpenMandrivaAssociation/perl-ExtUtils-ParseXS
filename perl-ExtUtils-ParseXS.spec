%define	modname	ExtUtils-ParseXS
%define modver	2.2206

Summary:	Converts Perl XS code into C code 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-CBuilder

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the constructs
necessary to let C functions manipulate Perl values and creates the glue
necessary to let Perl access those functions.  The compiler uses typemaps to
determine how to map C function parameters and variables to Perl values.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes INSTALL
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/*

