# Files

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Audio_Files.htm

# Files

Manage content stored on the Q-SYS Core processor. Stored audio is available for use by the Audio Player component, Public Address (PA) system, and any Softphones in your design.

**Note:** Administer the PA system â including global settings, page stations, PA zones, commands, command scheduling, and PA users â using Q-SYS Administrator, accessible from the Tools menu in Q-SYS Designer.

## Default Folders

Content is organized into folders, each containing files for a specific purpose:

* Audio â Stores audio for playback using the Audio Player component. (Audio Player can play back audio files stored in the other folders as well.)
* Messages â Stores audio files for playback using the PA Play Messages command.
* PageArchives â Stores previously played pages from the PA system, if archiving is enabled in the PA Global Settings, in the Virtual Page Station component, or with external control using the PA Remote API.
* Preambles â Stores audio files for playback using the PA Page command.
* Ringtones â Stores audio files for use by the Q-SYS Softphone, as configured in the Softphone Status/Control component.

## Managing Files and Folders

[Add Folders](javascript:void(0))

Click  to create a new folder within any of the default audio folders or at the root level of the default folders.

[Upload Files](javascript:void(0))

Click  to add files to a folder, or drag and drop files from your PC directly into a folder. You can select one or more files for uploading at a time.

**Tip:** After uploading files, you can easily move them by clicking and dragging to a subfolder or to a parent folder in the breadcrumbs.

#### Supported File Formats

You can upload audio files meeting these requirements:

* File types: .mp3, .wav, or .flac
* Sample size: 8, 16, 24, 32-bit fixed-point and 32-bit floating-point
* Sample rate: 48 kHz recommended
* Maximum file size: 1.5 GB

#### Storage Space for Files

The amount of space available for storing files on the Q-SYS Core is indicated in the top-right corner of the Files page. Storage space for files varies by Core model, the size of the media drive installed, and the size of the design file running on the Core.

The audio file time that the disk space can store depends entirely on your audio file format and number of tracks. For example, a 16-bit .wav file at 48 kHz uses approximately 5.76 MB per track per minute while a 128k bitrate MP3 file uses about 1 MB per minute.

[Play Back Files](javascript:void(0))

Click the  icon next to a file name to sample an audio file using your PC's soundcard.

[Rename Folders and Files](javascript:void(0))

Click  to rename a selected folder or file.

**Note:** The [Default Folders](#Default) cannot be renamed.

[Download Files](javascript:void(0))

Select one or more audio files, and then click  to download the files to your PC. You can also drag and drop files directly onto your PC's desktop.

**Note:** Folders cannot be selected and downloaded.

[Delete Folders and Files](javascript:void(0))

Click  to delete a selected folder or file.

**Note:** The [Default Folders](#Default) cannot be deleted.

[Viewing File Information](javascript:void(0))

Select a file or folder to view its information in the File Information tab. File information includes file type (.wav, .mp3, etc.), location, size, and creation and modification dates.

## Creating Playlists

You can create playlists for use by an Audio Player component in your design. You can add audio files to a playlist from any audio folder.

1. In the Playlists tab, click .
2. Type a unique playlist name, and then click Create.
3. Within any audio folder, select a single file or use the Ctrl key to select multiple files.
4. Either click and then select a playlist name, or drag the selected files into a playlist.
