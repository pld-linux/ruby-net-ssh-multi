%define pkgname net-ssh-multi
Summary:	Control multiple Net::SSH connections via a single interface
Name:		ruby-%{pkgname}
Version:	1.2.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	618b8f5fe6d80e6823bdf53c1d5d7c3d
URL:		https://github.com/net-ssh/net-scp
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Control multiple Net::SSH connections via a single interface.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGES.txt LICENSE.txt
%{ruby_vendorlibdir}/net/ssh/multi
%{ruby_vendorlibdir}/net/ssh/multi.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
