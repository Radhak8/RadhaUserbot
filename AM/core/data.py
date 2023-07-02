
import contextlib

from ..sql_helper.global_collectionjson import get_collection
from ..sql_helper.global_list import get_collection_list


def _sudousers_list():
    sudousers = {}
    with contextlib.suppress(AttributeError):
        sudousers = get_collection("sudousers_list").json
    return [int(chat) for chat in [*sudousers]]


def _vcusers_list():
    vcusers = {}
    with contextlib.suppress(AttributeError):
        vcusers = get_collection("vcusers_list").json
    return [int(chat) for chat in [*vcusers]]


def _users_list():
    sudousers = {}
    with contextlib.suppress(AttributeError):
        sudousers = get_collection("sudousers_list").json
    ulist = [int(chat) for chat in [*sudousers]]
    ulist.append("me")
    return list(ulist)


def blacklist_chats_list():
    blacklistchats = {}
    with contextlib.suppress(AttributeError):
        blacklistchats = get_collection("blacklist_chats_list").json
    return [int(chat) for chat in [*blacklistchats]]


def sudo_enabled_cmds():
    listcmds = get_collection_list("sudo_enabled_cmds")
    return list(listcmds)
