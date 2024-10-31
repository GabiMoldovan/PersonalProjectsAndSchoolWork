import re
from downloader.linkValidator.linkError import linkError


class validateLink:
    @staticmethod
    def validator(link: str) -> None:
        '''
        the function that checks the structure of the link in the text label
        :param link: link from the text label
        :return: None, sends the error back to the downloader so they catch in that try catch block and are raised
        by the interface
        '''
        errors = []

        patternLink = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]{11}$'
        rezLink = bool(re.match(patternLink, link))

        patternPlaylist = r'^(https?://)?(www\.)?(youtube\.com/playlist\?list=)[\w-]{10,34}$'
        rezPlaylist = bool(re.match(patternPlaylist, link))

        if rezPlaylist is False and rezLink is False:
            errors.append("Incorrect link to your video or playlist (make sure your playlist is set on public!)")

        if len(errors) > 0:
            raise linkError(errors)
