# TODO:
# - files section
# - rpm scripts
#
Summary:	Bacula - The Network Backup Solution
Name:		bacula
Version:	1.34.6
Release:	0.1
Epoch:		0
Group:		Networking/Utilities
License:	GPL v2
Source0:	http://dl.sourceforge.net/bacula/%{name}-%{version}.tar.gz
# Source0-md5:	9de593cb206df126a8e27774281c5bf6
Source1:	http://www.tux.org/pub/distributions/tinylinux/tomsrtbt/tomsrtbt-2.0.103.tar.gz
# Source1-md5:	d5ee50efb28986d564547d5da5de2483
Source2:	%{name}-manpages.tar.bz2
# Source2-md5:	e4dae86d6574b360e831efd3913e7f4c
Source10:	%{name}-dir.init
Source11:	%{name}-fd.init
Source12:	%{name}-sd.init
Source13:	%{name}.logrotate
URL:		http://www.bacula.org/
BuildRequires:	mtx
BuildRequires:	wxGTK2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	sqlite2-devel
BuildRequires:	libwrap-devel
BuildRequires:	zlib-devel
BuildRequires:	acl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glibc-static
BuildRequires:	acl-static
BuildRequires:	libwrap-static
BuildRequires:	libstdc++-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%package common
Summary:	Common files for bacula package
Group:		Networking/Utilities
Conflicts:	bacula-dir < %{epoch}:%{version}-%{release}
Conflicts:	bacula-fd < %{epoch}:%{version}-%{release}
Conflicts:	bacula-sd < %{epoch}:%{version}-%{release}
Conflicts:	bacula-console < %{epoch}:%{version}-%{release}

%description common
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files.

%package dir
Summary:	Bacula Director and Catalog services
Group:		Networking/Utilities
Prereq:		bacula-common = %{epoch}:%{version}-%{release}

%description dir
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Director is the program that supervises all the backup,
restore, verify and archive operations. The system administrator uses
the Bacula Director to schedule backups and to recover files. Catalog
services are comprised of the software programs responsible for
maintaining the file indexes and volume databases for all files backed
up. The Catalog services permit the System Administrator or user to
quickly locate and restore any desired file, since it maintains a
record of all Volumes used, all Jobs run, and all Files saved. This
build requires sqlite to be installed separately as the catalog
database.

%package console
Summary:	Bacula Console
Group:		Networking/Utilities
Prereq:		bacula-common = %{epoch}:%{version}-%{release}

%description console
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the text only console
interface.

%package console-wx
Summary:	Bacula wxWindows Console
Group:		Networking/Utilities
Prereq:		bacula-common = %{epoch}:%{version}-%{release}

%description console-wx
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Console is the program that allows the administrator or user to
communicate with the Bacula Director. This is the wxWindows GUI
interface.

%package fd
Summary:	Bacula File services (Client)
Group:		Networking/Utilities
Prereq:		bacula-common = %{epoch}:%{version}-%{release}

%description fd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula File services (or Client program) is the software program that
is installed on the machine to be backed up. It is specific to the
operating system on which it runs and is responsible for providing the
file attributes and data when requested by the Director. The File
services are also responsible for the file system dependent part of
restoring the file attributes and data during a recovery operation.
This program runs as a daemon on the machine to be backed up, and in
some of the documentation, the File daemon is referred to as the
Client (for example in Bacula configuration file).

%package sd
Summary:	Bacula Storage services
Group:		Networking/Utilities
Prereq:		bacula-common = %{epoch}:%{version}-%{release}

%description sd
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula Storage services consist of the software programs that perform
the storage and recovery of the file attributes and data to the
physical backup media or volumes. In other words, the Storage daemon
is responsible for reading and writing your tapes (or other storage
media, e.g. files). The Storage services runs as a daemon on the
machine that has the backup device (usually a tape drive).

%package rescue
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities
Requires:	coreutils
Requires:	util-linux
Requires:	bacula-fd

%description rescue
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for disaster recovery and builds rescue
floppy disks for bare metal recovery. This package includes tomsrtbt
(http://www.toms.net/rb/, by Tom Oehser, Tom@Toms.NET) to provide a
tool to build a boot floppy disk.

To create a boot disk run "./getdiskinfo" from the
%{_sysconfdir}/rescue directory (this is done when the package is
first installed), then run "./install.s" from the
%{_sysconfdir}/rescue/tomsrtbt/ directory. To make the bacula rescue
disk run "./make_rescue_disk --copy-static-bacula
- --copy-etc-files" from the %{_sysconfdir}/rescue directory. To
  recreate the rescue information for this system run ./getdiskinfo
  again.

%package updatedb
Summary:	Bacula - The Network Backup Solution
Group:		Networking/Utilities

%description updatedb
Bacula - It comes by night and sucks the vital essence from your
computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of
computer data across a network of computers of different kinds. In
technical terms, it is a network client/server based backup program.
Bacula is relatively easy to use and efficient, while offering many
advanced storage management features that make it easy to find and
recover lost or damaged files. Bacula source code has been released
under the GPL version 2 license.

This package installs scripts for updating older versions of the
bacula database.

%prep
%setup -q -a 1 -a 2
sed -i -e 's#wx-config#wxgtk2-2.4-config#g' configure*
sed -i -e 's#-lreadline -ltermcap#-lreadline#g' configure*

%build
# patches for the bundled sqlite scripts
# patch the make_sqlite_tables script for installation bindir
patch src/cats/make_sqlite_tables.in src/cats/make_sqlite_tables.in.patch
# patch the create_sqlite_database script for installation bindir
patch src/cats/create_sqlite_database.in src/cats/create_sqlite_database.in.patch
# patch the make_catalog_backup script for installation bindir
patch src/cats/make_catalog_backup.in src/cats/make_catalog_backup.in.patch
# patch the update_sqlite_tables script for installation bindir
patch src/cats/update_sqlite_tables.in src/cats/update_sqlite_tables.in.patch

CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/readline"
%configure \
	--with-scriptdir=%{_libexecdir}/%{name} \
	--disable-gnome \
	--disable-conio \
	--enable-smartalloc \
	--enable-wx-console \
	--with-readline \
	--with-tcp-wrappers \
	--with-working-dir=%{_var}/lib/%{name} \
	--with-dump-email="root@localhost" \
	--with-job-email="root@localhost" \
	--with-smtp-host=localhost \
	--with-pid-dir=/var/run \
	--with-subsys-dir=/var/lock/subsys \
	--with-sqlite \
	--enable-static-fd \
	--with-dir-password="#FAKE#DIR#PASSWORD#" \
        --with-fd-password="#FAKE#FD#PASSWORD#" \
        --with-sd-password="#FAKE#SD#PASSWORD#"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,logrotate.d,pam.d,security/console.apps}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rescue/tomsrtbt,updatedb}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# static daemon
strip src/filed/static-bacula-fd
install src/filed/static-bacula-fd $RPM_BUILD_ROOT%{_sysconfdir}/rescue/bacula-fd

install %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-dir
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-fd
install %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/bacula-sd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}

install scripts/bacula.png $RPM_BUILD_ROOT%{_pixmapsdir}/bacula.png

# install the rescue stuff, these are the rescue scripts
install rescue/linux/backup.etc.list $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/format_floppy $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/getdiskinfo $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/make_rescue_disk $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/restore_bacula $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/restore_etc $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/run_grub $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/run_lilo $RPM_BUILD_ROOT%{_sysconfdir}/rescue/
install rescue/linux/sfdisk.bz2 $RPM_BUILD_ROOT%{_sysconfdir}/rescue/

# this is the tom's root boot disk
install tomsrtbt-*/* $RPM_BUILD_ROOT%{_sysconfdir}/rescue/tomsrtbt/

# install the updatedb scripts
install updatedb/* $RPM_BUILD_ROOT%{_sysconfdir}/updatedb/

# manual
install -d html-manual
cp -a doc/html-manual/*.{html,jpg,gif,css} html-manual/

# drop some files
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/{gconsole,startmysql,stopmysql}

%pre common
# FIXME: dodawanie usera bacula /var/lib/bacula /bin/false

%postun common
# FIXME: del usera bacula

%post dir
umask 077
[ -s %{_localstatedir}/%{name}/bacula.db ] && \
        DB_VER=`echo "select * from Version;" | \
                sqlite %{_localstatedir}/%{name}/bacula.db | tail -n 1 2>/dev/null`
if [ -z "$DB_VER" ]; then
# grant privileges and create tables
        %{_libexecdir}/%{name}/grant_bacula_privileges > dev/null
        %{_libexecdir}/%{name}/create_bacula_database > dev/null
        %{_libexecdir}/%{name}/make_bacula_tables > dev/null
elif [ "$DB_VER" -lt "7" ]; then
        echo "Backing up bacula tables"
        echo ".dump" | sqlite %{_localstatedir}/%{name}/bacula.db | bzip2 > %{_localstatedir}/%{name}/bacula_backup.sql.bz2
        type=sqlite
        echo "Upgrading bacula tables"
        if [ "$DB_VER" -lt "6" ]; then
                if [ "$DB_VER" -lt "5" ]; then
                        %{_libexecdir}/%{name}/update_${type}_tables_4_to_5
                fi
                %{_libexecdir}/%{name}/update_${type}_tables_5_to_6
        fi
        %{_libexecdir}/%{name}/update_bacula_tables
        echo "If bacula works correctly you can remove the backup file %{_localstatedir}/%{name}/bacula_backup.sql.bz2"
fi
chown -R bacula:bacula %{_localstatedir}/%{name}
chmod -R u+rX,go-rwx %{_localstatedir}/%{name}

#%_post_service bacula-dir

%preun dir
#%_preun_service bacula-dir

%post fd
#%post_fix_config bacula-fd
#%_post_service bacula-fd

%preun fd
#%_preun_service bacula-fd

%post sd
#%post_fix_config bacula-sd
#%_post_service bacula-sd

%preun sd
#%_preun_service bacula-sd

%pre console
if [ -e %{_sysconfdir}/console.conf -a ! -e %{_sysconfdir}/bconsole.conf ]; then
        mv %{_sysconfdir}/console.conf %{_sysconfdir}/bconsole.conf
fi

#%post console
#%post_fix_config bconsole


%post updatedb
echo "The database update scripts were installed to %{_sysconfdir}/updatedb"

%clean
rm -rf $RPM_BUILD_ROOT

%post rescue
# link our current installed conf file to the rescue directory
ln -s %{_sysconfdir}/bacula-fd.conf %{_sysconfdir}/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd %{_sysconfdir}/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
rm -f %{_sysconfdir}/rescue/bacula-fd.conf
rm -f %{_sysconfdir}/rescue/partition.*
rm -f %{_sysconfdir}/rescue/format.*
rm -f %{_sysconfdir}/rescue/mount_drives
rm -f %{_sysconfdir}/rescue/start_network
rm -f %{_sysconfdir}/rescue/sfdisk
rm -rf %{_sysconfdir}/rescue/diskinfo/*

%files common
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%attr(755, root, root) %{_sbindir}/btraceback
%attr(755, root, root) %{_sbindir}/bsmtp
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/btraceback.gdb
%attr(700, bacula, bacula) %dir %{_localstatedir}/%{name}

%files dir
%defattr(644,root,root,755)
%doc ChangeLog CheckList ReleaseNotes kernstodo
%doc doc/*.pdf doc/manual examples
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/%{name}/bacula-dir.conf
%ghost %{_sysconfdir}/%{name}/.pw.sed
%config(noreplace) %{_sysconfdir}/logrotate.d/bacula-dir
%{_mandir}/man8/bacula-dir.8*
%{_mandir}/man1/dbcheck.1*
%defattr (755, root, root)
%config(noreplace) %{_initrddir}/bacula-dir
%attr(755,root,root) %{_sbindir}/bacula-dir
%attr(755,root,root) %{_sbindir}/dbcheck
%{_libexecdir}/%{name}/create_sqlite_database
%{_libexecdir}/%{name}/drop_sqlite_database
%{_libexecdir}/%{name}/drop_sqlite_tables
%{_libexecdir}/%{name}/grant_sqlite_privileges
%{_libexecdir}/%{name}/make_sqlite_tables
%{_libexecdir}/%{name}/update_sqlite_tables*
%{_libexecdir}/%{name}/create_bacula_database
%{_libexecdir}/%{name}/drop_bacula_database
%{_libexecdir}/%{name}/drop_bacula_tables
%{_libexecdir}/%{name}/grant_bacula_privileges
%{_libexecdir}/%{name}/make_bacula_tables
%{_libexecdir}/%{name}/update_bacula_tables
%{_libexecdir}/%{name}/make_catalog_backup
%{_libexecdir}/%{name}/delete_catalog_backup
%attr(644, root, root) %{_libexecdir}/%{name}/query.sql

%files fd
%defattr(644,root,root,755)
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/%{name}/bacula-fd.conf
%config(noreplace) %{_initrddir}/bacula-fd
%attr(755,root,root) %{_sbindir}/bacula-fd
%attr(644, root, root) %{_mandir}/man8/bacula-fd.8*

%files sd
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/%{name}/bacula-sd.conf
%config(noreplace) %{_initrddir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bacula-sd
%attr(755,root,root) %{_sbindir}/bcopy
%attr(755,root,root) %{_sbindir}/bextract
%attr(755,root,root) %{_sbindir}/bls
%attr(755,root,root) %{_sbindir}/bscan
%attr(755,root,root) %{_sbindir}/btape
%{_libexecdir}/%{name}/mtx-changer
%defattr(644, root,root, 755)
%{_mandir}/man8/bacula-sd.8*
%{_mandir}/man1/bcopy.1*
%{_mandir}/man1/bextract.1*
%{_mandir}/man1/bls.1*
%{_mandir}/man1/bscan.1*
%{_mandir}/man1/btape.1*

%files console
%defattr(644,root,root,755)
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/%{name}/bconsole.conf
%attr(755, root, root) %{_sbindir}/bconsole
%config(noreplace) %{_sysconfdir}/security/console.apps/bconsole
%config(noreplace) %{_sysconfdir}/pam.d/bconsole
%verify(link) %{_bindir}/bconsole
%{_mandir}/man1/bconsole.1*


%files console-wx
%defattr(644,root,root,755)
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_menudir}/bacula-console-wx
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/%{name}/wx-console.conf
%attr(755, root, root) %{_sbindir}/wx-console
%config(noreplace) %{_sysconfdir}/security/console.apps/wx-console
%config(noreplace) %{_sysconfdir}/pam.d/wx-console
%verify(link) %{_bindir}/wx-console
%{_mandir}/man1/wx-console.1*

%files rescue
%defattr(644,root,root,755)
%{_sysconfdir}/rescue

%files updatedb
%defattr(644,root,root,755)
%{_sysconfdir}/updatedb
