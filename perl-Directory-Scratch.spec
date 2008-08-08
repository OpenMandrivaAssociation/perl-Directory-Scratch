%define module   Directory-Scratch
%define version    0.14
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl Module to generate self-cleaning scratch space for tests
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Directory/%{module}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::stat)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
When writing test suites for modules that operate on files, it's often
inconvenient to correctly create a platform-independent temporary storage
space, manipulate files inside it, then clean it up when the test exits. The
inconvenience usually results in tests that don't work everwhere, or worse, no
tests at all.

This module aims to eliminate that problem by making it easy to do things right.
%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Directory

