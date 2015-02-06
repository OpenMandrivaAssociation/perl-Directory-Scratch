%define upstream_name    Directory-Scratch
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.15
Release:	3

Summary:	Perl Module to generate self-cleaning scratch space for tests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Directory/Directory-Scratch-0.15.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::stat)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
When writing test suites for modules that operate on files, it's often
inconvenient to correctly create a platform-independent temporary storage
space, manipulate files inside it, then clean it up when the test exits. The
inconvenience usually results in tests that don't work everwhere, or worse, no
tests at all.

This module aims to eliminate that problem by making it easy to do things
right.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Directory


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 681425
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 402136
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2009.0
+ Revision: 268440
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.0
+ Revision: 217982
- update to new version 0.14

  + Michael Scherer <misc@mandriva.org>
    - enhance description and summary

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.0
+ Revision: 213728
- import perl-Directory-Scratch


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.0
- first mdv release

