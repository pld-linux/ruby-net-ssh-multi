%define pkgname net-ssh-multi
Summary:	Control multiple Net::SSH connections via a single interface
Name:		ruby-%{pkgname}
Version:	1.2.0
Release:	1
License:	Distributable
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1c8dbed63e805bf6a663cde2c76d4b45
URL:		https://github.com/net-ssh/net-scp
Requires:	ruby-mocha
Requires:	ruby-net-ssh >= 2.6.5
Requires:	ruby-net-ssh-gateway >= 1.2.0
Requires:	ruby-test-unit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Control multiple Net::SSH connections via a single interface.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGES.txt LICENSE.txt
%{ruby_vendorlibdir}/net/ssh/multi.rb
%{ruby_vendorlibdir}/net/ssh/multi