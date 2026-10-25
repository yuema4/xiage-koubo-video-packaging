"""Package approved static comparisons; never copy source footage or subtitles."""
import argparse
import shutil
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('source', type=Path, help='Approved comparison export directory')
args = parser.parse_args()
dest = Path(__file__).resolve().parents[1] / 'assets' / 'landscape'
dest.mkdir(parents=True, exist_ok=True)
styles = ['capsule', 'block', 'tech', 'minimal']
for scene in range(1, 5):
    shutil.copy2(args.source / f'场景{scene}-四风格对比.jpg', dest / f'comparison-{scene:02}.jpg')
    for style in styles:
        for source_dir, suffix in [('实拍预览', 'preview'), ('卡片特写', 'detail')]:
            with Image.open(args.source / source_dir / f'{style}-{scene}.png') as im:
                im.convert('RGB').save(dest / f'{style}-{scene:02}-{suffix}.jpg', quality=92, optimize=True)
shutil.copy2(args.source / 'Lucide-LICENSE.txt', dest / 'Lucide-LICENSE.txt')
print('Packaged 16 composites, 16 close-ups, 4 comparison sheets, and icon license.')
