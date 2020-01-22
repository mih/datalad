# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""
"""
from datalad.utils import Path


class OperationsBase(object):
    """Abstract class with the desired API for operations.

    Any path-like argument must be a pathlib object.

    Method parameters must be verbose or generic enough to be translatable
    to non-POSIX systems, such as Windows.
    """
    def __init__(self, cwd=None):
        """
        Parameters
        ----------
        cwd : Path or None
          Current working directory to resolve any relative paths against.
          If None, the process working directory (PWD) is used.
        """
        self._cwd = Path.cwd() if cwd is None else cwd

    def make_directory(self, path, force=False):
        """Create a new directory

        Parameters
        ----------
        path : Path
          Location at which to create a directory.
        force : bool
          Enforce creation of directory, even when it already exists,
          or if parent directories are missing.
        """
        raise NotImplementedError

    def exists(self, path):
        """Test if something exists at the given path

        Parameters
        ----------
        path : Path
          Path to test.

        Returns
        -------
        bool
          True, if the path exists (even in case of a broken symlink), False
          otherwise.
        """
        raise NotImplementedError

    def remove(self, path, recursive=False):
        """Remove the given path

        Parameters
        ----------
        path : Path
          Path to remove.
        recursive : bool
          If True, everything underneath `path` is also removed, If False,
          `path` removal might fail with present content.
        """
        raise NotImplementedError

    def change_permissions(self, path, mode, recursive=False):
        """Change the permissions for a path

        Parameters
        ----------
        path : Path
          Path to change permissions of.
        mode : str
          Recognized label for a permission mode, such as 'user_readonly'.
        recursive : bool
          Apply change recursively to all content underneath the path, too.
        """
        raise NotImplementedError

    def change_group(self, path, label, recursive=False):
        """Change the group ownership for a path

        Parameters
        ----------
        path : Path
          Path to change ownership of.
        label : str
          Name of the group.
        recursive : bool
          Apply change recursively to all content underneath the path, too.
        """
        raise NotImplementedError


class RemoteOperationsBase(OperationsBase):
    """Abstract class with the desired API for remote operations.
    """
    def __init__(self, cwd=None, remote_cwd=None):
        """
        Parameters
        ----------
        cwd : Path or None
          Local working directory to resolve any relative paths against.
          If None, the process working directory (PWD) is used.
        remote_cwd : Path or None
          Remote working directory to resolve any remote relative paths
          against. If None, the process working directory (PWD) of the
          remote connection is used.
        """
        super(RemoteOperationsBase, self).__init__(cwd=cwd)

        self._remote_cwd = remote_cwd
