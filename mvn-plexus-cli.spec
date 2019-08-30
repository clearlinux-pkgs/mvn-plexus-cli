#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-cli
Version  : 1.6
Release  : 2
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-cli/1.6/plexus-cli-1.6.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-cli/1.6/plexus-cli-1.6.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-cli/1.6/plexus-cli-1.6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plexus-cli-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-cli package.
Group: Data

%description data
data components for the mvn-plexus-cli package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6/plexus-cli-1.6.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-cli/1.6/plexus-cli-1.6.pom
