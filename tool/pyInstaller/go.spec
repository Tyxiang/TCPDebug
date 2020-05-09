# -*- mode: python -*-

block_cipher = None


a = Analysis(['go.py'],
             pathex=['D:\\My Documents\\1_Personal\\3_Process\\4_Open\\TCPDebug\\_pyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='go',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
