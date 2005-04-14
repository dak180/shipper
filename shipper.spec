Name: shipper
Version: 0.10
Release: 1
URL: http://www.catb.org/~esr/shipper/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Utilities
Summary: automated shipping of open-source project releases
Requires: lftp, openssh-clients, freshmeat-submit
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
#Keywords: packaging, distribution

%description 
shipper is a power distribution tool for developers with multiple
projects who do frequent releases.  It automates the tedious process
of shipping a software release to several standard places, including
ibiblio, the Red Hat submission directory, and your own hosted
website.  It also knows how to post a release announcement to
freshmeat.net via freshmeat-submit.  Two auxiliary tools, buildrpms
and rpm2lsm, build RPMs and generate LSM files from them respectively.

%prep 
%setup -q

%build
make %{?_smp_mflags} shipper.1 rpm2lsm.1

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"%{_bindir}
mkdir -p "$RPM_BUILD_ROOT"%{_mandir}/man1/
cp shipper rpm2lsm buildrpms "$RPM_BUILD_ROOT"%{_bindir}
cp shipper.1 rpm2lsm.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/shipper
%{_bindir}/rpm2lsm
%{_bindir}/buildrpms
%{_mandir}/man1/shipper.1*
%{_mandir}/man1/rpm2lsm.1*

%changelog
* Thu Apr 14 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 0.10-1
- Generate correct download directories in a Freshmeat announcement for a 
  Berlios project.  Check version in makefile as well as Makefile.

* Thu Mar  3 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 0.9-1
- The Channels variable is gone. There are no longer default public channels;
  you put the ones you want in your Destinations variable.  For safety's sake
  the force (-f) option is also gone; generated deliverables are now built 
  unconditionally, and you must explicitly make sure no index.html exists 
  in order to get one generated.  There is now a "berlios" channel.

* Tue Feb  1 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 0.8-1
- Strip trailing edit-mode lines out of RPM spec files.

* Thu Jan 27 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 0.7-1
- Now handles packages that generate multiple binary RPMs correctly.

* Sat Aug 21 2004 Eric S. Raymond <esr@snark.thyrsus.com> 0.6-1
- Fixed a minor bug in the generation of lftp commands.  Also, generate
  a To line into email announcement.  Mailman doesn't like implicit
  addressing. 

* Fri Feb 6 2004 Eric S. Raymond <esr@snark.thyrsus.com> 0.5-1
- Added security check so the ~/.shipper and .shipper files can't be used
  for privilege elevation.  Fixed upload omission bug in case where neither 
  -n nor -f was on and the webpage wasn't being built.  Deliverables 
  created for upload are deleted at end of run.

* Sun Jan 11 2004 Eric S. Raymond <esr@snark.thyrsus.com> 0.4-1
- Correct extraction of freshmeat name.  Build generated deliverables
  only if we know they will be needed. Help is now available at the 
  freshmeat-focus prompt.

* Sat Jan 10 2004 Eric S. Raymond <esr@snark.thyrsus.com> 0.3-1
- First alpha release of unified shipper package.  It can ship itself.

* Wed Dec 17 2003 Eric S. Raymond <esr@snark.thyrsus.com>
- rpm2lsm now grabs an RPM from the current directory if no argument,
  and parses an AUTHORS file if present (GNU convention).  Also,
  this release fixes a bug in USERNAME handling.

* Thu Aug  1 2002 Eric S. Raymond <esr@snark.thyrsus.com>
- Initial release of rpm2lsm, since folded into shipper package.

# The following sets edit modes for GNU EMACS
# Local Variables:
# mode:rpm-spec
# End:
