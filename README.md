# stacki3

Simple stack layout for i3/sway wm.

## How it works

![Preview](./preview.gif)
(proportion set with `stacki3 45`)

_stacki3_ does only 3 things:

- when there is only **one** window set split to `horizontal`
- when there are exactly **two** windows set split to `vertical`
- _optionally_ when proportion is set with `width` argument (like in preview) resize the second window

That's it!

## Instalation

1. Install the package

```bash
pip install --user stacki3
```

2. Inside your i3/sway config add

```i3
exec_always stacki3 45
```

3. Restart i3/sway
