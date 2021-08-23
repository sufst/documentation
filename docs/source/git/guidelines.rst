Contributing Guidelines
=======================

This page contains all needed Guidelines for contrubuting to SUFST's codebases. These rules should be followed by **all team members** - without exemptions - in order to keep an organised and always evolving software development environment. 

.. caution:: From this point onwards, mentioning **"Committee"** means one of the 4 Heads of the Electronics Department, as written on the team's `SharePoint homepage <https://sotonac.sharepoint.com/teams/sufst>`_ 

Writing Code
------------

**Rules for contributing code:**

1. Always **make a NEW BRANCH** for changes to an existing or new codebase. 

.. attention:: 

   Never modify code on the default ``main`` branch. 

   This **will not work** - you won't be able to push your changes - and you will end up having to revert back!


New branches should follow a naming scheme of ``issue-<issue-number>-<description>``. For example: ``issue-30-dashboard``.

If an issue doesn't exist for a feature you are trying to add, then please make one keeping in mind the instructions outlined in the Issues_ section below. 

2. Make it a habit to **frequently commit** and push your changes to the remote branch. At the same time, please keep commit messages PG-13. (I know this will not be possible sometimes, but let's not do that frequently.)
 

3. All code should be styled as in the original codebase. 
  
.. note:: 

   - If working on an **existing project**, please follow the styling guides and file structure / format that the previous contributors have agreed upon. 
   - If working on a **new project**, feel free to use whatever suites the project team more. However, if not sure, you are advised to ask a Committee member out for more information. 

4. The **GPL-3.0 copyright** block should written as a comment. on the **TOP OF EVERY FILE**, especially if the codebase is intended (or already available) for open-source distribution on GitHub. For example you see `this <https://github.com/sufst/wireless-telemetry-gui/blob/main/src/index.js>`_ file. 

      Southampton University Formula Student Team 

      Copyright (C) <CURRENT_YEAR> SUFST
      
      This program is free software: you can redistribute it and/or modify
      it under the terms of the GNU General Public License as published by
      the Free Software Foundation, either version 3 of the License, or
      (at your option) any later version.

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <https://www.gnu.org/licenses/>


Issues
------

Every team member is **strongly encouraged** to open new issues on GitHub on projects they are working on, or on other should they have something to comment on - suggest. To keep the issue pages on each repository manageable, please follow this simple points: 

1. Always say whether you're mentioning a **bug** or a **new feature**. In the future, issue templates will be set-up for you to follow in both cases. 

.. note:: 

   - If mentioning a **bug**, write on how to reproduce it - as detailed as possible. 
   - If mentioning a **new feature**, write on *how* this will help and *why* it is needed. 

2. Add the appropriate **labels** on the issue. For example, if talking about a new feature, the default *enhancement* label should be used. 

3. If the bug or feature is something you feel comfortable to work on, **feel free to mention it in the issue description**. This way a Committee member will know this issue can be worked on and will assign you. Please don't auto-assign yourselves issues. 

Pull Requests
-------------

Pull requests are meant to help Committee review new code to be merged into the ``main`` branch. When finishing work on a specific branch, you'll need to open a Pull Request to let the Committee know your code is ready to be brought into production.

.. caution:: 

   When opening a Pull Request you'll notice that you won't be able to merge these changes yourselves. This is so only code reviewed and approved by a Committee member can be brought into ``main``. 

Having the Pull Request open **feel free to request review** by the Committee member responsible for the project you are working on. Each repository is set up in a way that it **requires an approved review** before a Pull Request can be merged. After requesting review and opening the PR, don't hesitate to message the Committe member or poke them on Team - Discord so they add merging your code into their agenda. 

If the reviewer of your Pull Requests requests code changes, you'll to push a new commit with these changes before they can go ahead with the merge. 
