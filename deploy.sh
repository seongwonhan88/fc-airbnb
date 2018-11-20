#!/usr/bin/env bash
git add -f .secrets/
eb deploy --profile ebfc --staged
git reset HEAD .secrets/
