%define	upstream_name	 ExtUtils-ParseXS
%define upstream_version 2.2206

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 8

Summary:	Converts Perl XS code into C code 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-CBuilder
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
ExtUtils::ParseXS will compile XS code into C code by embedding the constructs
necessary to let C functions manipulate Perl values and creates the glue
necessary to let Perl access those functions.  The compiler uses typemaps to
determine how to map C function parameters and variables to Perl values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.220.600-7mdv2012.0
+ Revision: 765233
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.220.600-6
+ Revision: 763743
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.220.600-5
+ Revision: 667133
- mass rebuild

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.600-4mdv2011.0
+ Revision: 597096
- rebuild

* Wed Jul 28 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.600-3mdv2011.0
+ Revision: 562424
- rebuild

* Wed Jul 21 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.600-2mdv2011.0
+ Revision: 556438
- rebuild for perl 5.12

* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.600-1mdv2011.0
+ Revision: 551220
- update to 2.2206

* Thu Mar 11 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.500-1mdv2010.1
+ Revision: 518075
- update to 2.2205

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.300-1mdv2010.1
+ Revision: 504487
- update to 2.2203

* Fri Jan 29 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.200-1mdv2010.1
+ Revision: 497904
- update to 2.2202

* Wed Jan 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.100-1mdv2010.1
+ Revision: 496996
- update to 2.2201

* Tue Jan 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.220.0-1mdv2010.1
+ Revision: 490072
- update to 2.22

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.210.0-1mdv2010.1
+ Revision: 460725
- update to 2.21

* Tue Sep 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.200.401-1mdv2010.0
+ Revision: 442938
- update to 2.200401

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.200.200-1mdv2010.0
+ Revision: 398840
- update to 2.2002

* Sun Jul 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.200.0-1mdv2010.0
+ Revision: 395036
- adding missing buildrequires
- update to 2.20
- using %%perl_convert_version
- fixed license field

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.19-2mdv2009.0
+ Revision: 223716
- rebuild

* Mon Feb 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.19-1mdv2008.1
+ Revision: 170116
- update to new version 2.19

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.18-1mdv2008.0
+ Revision: 20079
- 2.18


* Tue Oct 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.16-1mdv2007.0
+ Revision: 71730
+ Status: not released
- 2.16
- Import perl-ExtUtils-ParseXS

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.15-1mdk
- 2.15

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.14-2mdk
- Fix BuildRequires

* Tue Oct 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.14-1mdk
- New release 2.14

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.13-1mdk
- New release 2.13

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdk
- new version
- fix source url
- better url
- better summary
- fix directory ownership
- spec cleanup
- enable tests
- fix buildrequires
- better description

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.11-1mdk
- 2.11

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.10-1mdk
- 2.10

* Thu Mar 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.09-1mdk
- 2.09

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 2.08-1mdk
- 2.08

* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.07-1mdk
- 2.07

