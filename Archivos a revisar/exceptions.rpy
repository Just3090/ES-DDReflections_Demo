




python early:

    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive
        
        def __str__(self):
            return "'" + self.archive + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
