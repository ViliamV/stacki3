# stacki3

Simple stack layout for i3/sway wm.

## How it works

The main idea is this - I only want max two columns on the screen.
More windows should be spawn vertically.

![Preview](./preview.gif)

(proportion set with `stacki3 45`)

_stacki3_ does only 3 things:

- when there is only **one** window set split to `horizontal`
- when there are exactly **two** windows set split to `vertical` on both windows
- _optionally_ when proportion is set with `width` argument (like in preview) resize the right window

That's it!

## Instalation

1. Install the package

```bash
pip install --user stacki3
```

2. Inside your i3/sway config add

```i3
# Default with splitting 50:50
exec stacki3
# OR
# Split first two windows 55:45
exec stacki3 45
```

3. Log out and log back in

## Inspiration

[i3-master-stack](https://github.com/windwp/i3-master-stack)
[autotiling](https://github.com/nwg-piotr/autotiling)
