# -*- mode: python -*-

a = Analysis(['twedit_plus_plus.py'],
             pathex=['/Users/m/qt5-demo/tw'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
             
             
##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################             

a.datas += extra_datas('themes')
a.datas += [("dummy_application","/Users/m/qt5-demo/dummy_application/dist/dummy_application","DATA")]             


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='twedit_plus_plus',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icons/twedit-new-128.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='twedit_plus_plus')
app = BUNDLE(coll,
             name='twedit_plus_plus.app',
             icon='icons/twedit-new-128.icns')



# # # a = Analysis(['twedit_plus_plus.py'],
# # #              pathex=['/Users/m/qt5-demo/tw'],
# # #              hiddenimports=[],
# # #              hookspath=None,
# # #              runtime_hooks=None)
             
# # # ##### include mydir in distribution #######
# # # def extra_datas(mydir):
# # #     def rec_glob(p, files):
# # #         import os
# # #         import glob
# # #         for d in glob.glob(p):
# # #             if os.path.isfile(d):
# # #                 files.append(d)
# # #             rec_glob("%s/*" % d, files)
# # #     files = []
# # #     rec_glob("%s/*" % mydir, files)
# # #     extra_datas = []
# # #     for f in files:
# # #         extra_datas.append((f, f, 'DATA'))

# # #     return extra_datas
# # # ###########################################             

# # # a.datas += extra_datas('themes')
# # # a.datas += [("dummy_application","/Users/m/qt5-demo/dummy_application/dist/dummy_application","DATA")]             




# # # pyz = PYZ(a.pure)
# # # exe = EXE(pyz,
# # #           a.scripts,
# # #           exclude_binaries=True,
# # #           name='twedit_plus_plus',
# # #           debug=False,
# # #           strip=None,
# # #           upx=True,
# # #           console=True , icon='icons/twedit-new-128.icns')
# # # coll = COLLECT(exe,
# # #                a.binaries,
# # #                a.zipfiles,
# # #                a.datas,
# # #                strip=None,
# # #                upx=True,
# # #                name='twedit_plus_plus')
               
# # # app = BUNDLE(coll,
# # #              name='twedit_plus_plus.app',
# # #              icon='icons/twedit-new-128.icns')
