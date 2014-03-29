# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

########################################################################
###### This file is generated. Manual changes will likely be lost. #####
########################################################################

import logging
log = logging.getLogger(__name__)

import uritemplate

import PyGithub.Blocking.BaseGithubObject
import PyGithub.Blocking.Parameters
import PyGithub.Blocking.PaginatedList
import PyGithub.Blocking._receive as rcv

import PyGithub.Blocking.GitBlob


class GitTree(PyGithub.Blocking.BaseGithubObject.UpdatableGithubObject):
    """
    Base class: :class:`.UpdatableGithubObject`

    Derived classes: none.

    Methods and attributes returning instances of this class:
      * :attr:`.GitCommit.tree`
      * :meth:`.GitTree.create_modified_copy`
      * :attr:`.GitTree.tree`
      * :meth:`.Repository.create_git_tree`
      * :meth:`.Repository.get_git_tree`
    """

    class GitSubmodule(PyGithub.Blocking.BaseGithubObject.SessionedGithubObject):
        """
        Methods and attributes returning instances of this class:
          * :attr:`.GitTree.tree`
        """

        def _initAttributes(self, mode=None, path=None, sha=None, type=None, **kwds):
            super(GitTree.GitSubmodule, self)._initAttributes(**kwds)
            self.__mode = rcv.Attribute("GitTree.GitSubmodule.mode", rcv.StringConverter, mode)
            self.__path = rcv.Attribute("GitTree.GitSubmodule.path", rcv.StringConverter, path)
            self.__sha = rcv.Attribute("GitTree.GitSubmodule.sha", rcv.StringConverter, sha)
            self.__type = rcv.Attribute("GitTree.GitSubmodule.type", rcv.StringConverter, type)

        @property
        def mode(self):
            """
            :type: :class:`string`
            """
            return self.__mode.value

        @property
        def path(self):
            """
            :type: :class:`string`
            """
            return self.__path.value

        @property
        def sha(self):
            """
            :type: :class:`string`
            """
            return self.__sha.value

        @property
        def type(self):
            """
            :type: :class:`string`
            """
            return self.__type.value

    def _initAttributes(self, mode=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, tree=rcv.Absent, type=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitTree, self)._initAttributes(**kwds)
        self.__mode = rcv.Attribute("GitTree.mode", rcv.StringConverter, mode)
        self.__path = rcv.Attribute("GitTree.path", rcv.StringConverter, path)
        self.__sha = rcv.Attribute("GitTree.sha", rcv.StringConverter, sha)
        self.__tree = rcv.Attribute("GitTree.tree", rcv.ListConverter(rcv.KeyedStructureUnionConverter("type", dict(blob=rcv.ClassConverter(self.Session, PyGithub.Blocking.GitBlob.GitBlob), commit=rcv.StructureConverter(self.Session, GitTree.GitSubmodule), tree=rcv.ClassConverter(self.Session, GitTree)))), tree)
        self.__type = rcv.Attribute("GitTree.type", rcv.StringConverter, type)
        self.__url = rcv.Attribute("GitTree.url", rcv.StringConverter, url)

    def _updateAttributes(self, eTag, mode=rcv.Absent, path=rcv.Absent, sha=rcv.Absent, tree=rcv.Absent, type=rcv.Absent, url=rcv.Absent, **kwds):
        super(GitTree, self)._updateAttributes(eTag, **kwds)
        self.__mode.update(mode)
        self.__path.update(path)
        self.__sha.update(sha)
        self.__tree.update(tree)
        self.__type.update(type)
        self.__url.update(url)

    @property
    def mode(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__mode.needsLazyCompletion)
        return self.__mode.value

    @property
    def path(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__path.needsLazyCompletion)
        return self.__path.value

    @property
    def sha(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__sha.needsLazyCompletion)
        return self.__sha.value

    @property
    def tree(self):
        """
        :type: :class:`list` of :class:`.GitTree` or :class:`.GitBlob` or :class:`.GitSubmodule`
        """
        self._completeLazily(self.__tree.needsLazyCompletion)
        return self.__tree.value

    @property
    def type(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__type.needsLazyCompletion)
        return self.__type.value

    @property
    def url(self):
        """
        :type: :class:`string`
        """
        self._completeLazily(self.__url.needsLazyCompletion)
        return self.__url.value

    def create_modified_copy(self, tree):
        """
        Calls the `POST /repos/:owner/:repo/git/trees <http://developer.github.com/v3/git/trees#create-a-tree>`__ end point.

        The following methods also call this end point:
          * :meth:`.Repository.create_git_tree`

        :param tree: mandatory :class:`list` of :class:`dict`
        :rtype: :class:`.GitTree`
        """

        tree = PyGithub.Blocking.Parameters.normalizeList(PyGithub.Blocking.Parameters.normalizeDict, tree)

        url = uritemplate.expand("https://api.github.com/repos/{owner}/{repo}/git/trees", owner=self.owner.login, repo=self.name)
        postArguments = PyGithub.Blocking.Parameters.dictionary(base_tree=self.sha, tree=tree)
        r = self.Session._request("POST", url, postArguments=postArguments)
        return GitTree(self.Session, r.json(), r.headers.get("ETag"))
