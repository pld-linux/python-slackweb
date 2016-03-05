%define 	module	slackweb
Summary:	Slack Bot for WebHook
Name:		python-%{module}
Version:	1.0.5
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/slackweb/slackweb-%{version}.tar.gz
# Source0-md5:	f02a62939376eccd1f70e61ee655f066
URL:		https://github.com/satoshi03/slack-python-webhook
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Very simple Slack client by using incoming-webhook.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/slackweb
%{py_sitescriptdir}/slackweb-%{version}-py*.egg-info
