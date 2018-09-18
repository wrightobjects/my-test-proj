init:
    python:
        class ProportionalScale(im.ImageBase):
            def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
                img = im.image(imgname)
                super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
                self.imgname = imgname
                self.image = img
                self.maxwidth = int(maxwidth)
                self.maxheight = int(maxheight)
                self.bilinear = bilinear

            def load(self):
                child = im.cache.get(self.image)
                currentwidth, currentheight = child.get_size()
                xscale = 1.0
                yscale = 1.0
                if (currentwidth > self.maxwidth):
                    xscale = float(self.maxwidth) / float(currentwidth)
                if (currentheight > self.maxheight):
                    yscale = float(self.maxheight) / float(currentheight)
                if (xscale < yscale):
                    minscale = xscale
                else:
                    minscale = yscale
                newwidth = currentwidth * minscale
                newheight = currentheight * minscale
                #Debug code to see when the loading really happens
                #renpy.log("Loading image %s from %f x %f to %f x %f" % (self.imgname, currentwidth , currentheight , newwidth, newheight))

                if self.bilinear:
                    try:
                        renpy.display.render.blit_lock.acquire()
                        rv = renpy.display.scale.smoothscale(child, (newwidth, newheight))
                    finally:
                        renpy.display.render.blit_lock.release()
                else:
                    try:
                        renpy.display.render.blit_lock.acquire()
                        rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
                    finally:
                        renpy.display.render.blit_lock.release()
                return rv

            def predict_files(self):
                return self.image.predict_files()
