import randf_pagedimensions as pd
import tinycss
import os

class Styler:
    def __init__(self):
        self.pageDim = {
            # Sizes ordered as WxH in cm
            'a0': pd.PageDimensions(84.1, 118.9),
            'a1': pd.PageDimensions(59.4, 84.1),
            'a2': pd.PageDimensions(42.0, 59.4),
            'a3': pd.PageDimensions(29.7, 42.0),
            'a4': pd.PageDimensions(21.0, 29.7),
            'a5': pd.PageDimensions(14.8, 21.0),
            'a6': pd.PageDimensions(10.5, 14.8),
            'b0': pd.PageDimensions(100.0, 141.4),
            'b1': pd.PageDimensions(59.4, 84.1),
            'b2': pd.PageDimensions(42.0, 59.4),
            'b3': pd.PageDimensions(29.7, 42.0),
            'b4': pd.PageDimensions(21.0, 29.7),
            'b5': pd.PageDimensions(14.8, 21.0),
            'b6': pd.PageDimensions(10.5, 14.8),
            'elevenseventeen': pd.PageDimensions(21.59, 27.94),
            'legal': pd.PageDimensions(21.59, 35.56),
            'letter': pd.PageDimensions(27.94, 43.1)
        }
        self.theme = 'light'
        self.margin = 'normal'
        self.top = 2.0
        self.left = 2.0
        self.pagesize = 'letter'
        self.orientation = 'portrait' # One of ['portrait', 'landscape']
        self.pgnum = False
        self.title = 'New Document'
        self.template = ''
        self.width = self.__set_width()
        self.height = self.__set_height()


    @property
    def theme(self):
        return self._theme
    
    @theme.setter
    def theme(self, theme_fn):
        """ Sets a new theme for the document """
        # Check if the file passed in exists
        filename = "themes/" + theme_fn + ".css"
        if (os.path.exists(filename) == False):
            print("[PARSER_ERR] Could not find theme file '{}'. Please make sure that the theme is in the theme/ folder. Falling back on default theme.".format(filename))
            return

        # Open and read the new themesheet from the themes/ folder
        f = open(filename, "r")
        new_theme = f.read()
        f.close()

        # Validate the CSS for the document and set the CSS if it is valid
        verifier = tinycss.make_parser('page3')
        parsed_contents = verifier.parse_stylesheet(new_theme)
        self._theme = new_theme

        """
        if parsed_contents.errors == []:
            self._theme = new_theme
        else:
            print('[PARSER_ERR] {} errors were encountered when attempting to parse the stylesheet. The following errors are:'.format(len(parsed_contents.errors)))
            for i in parsed_contents.errors:
                print("  {}".format(i))
        """                

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, new_margin):
        """ Sets a new margin """
        self._margin = new_margin

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, new_TB):
        """ Sets new top value """
        self._top = new_TB

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new_LR):
        """ Sets new left value """
        self._left = new_LR

    @property
    def pagesize(self):
        return self._pagesize

    @pagesize.setter
    def pagesize(self, new_pagesize):
        """ Sets a new pagesize """
        self._pagesize = new_pagesize

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, new_orientation):
        """ Sets a new orientation for the document """
        self._orientation = new_orientation

    @property
    def pgnum(self):
        return self._pgnum
    
    @pgnum.setter
    def pgnum(self, onOrOff: bool):
        """ Turns the page numbers on or off """
        self._pgnum = onOrOff

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        """ Sets the title of the document """
        self._title = new_title

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, new_template):
        """ Sets the preprocessor command template of the document """
        self._template = new_template

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if self.orientation == 'portrait':
            self.__set_width()
        if self.orientation == 'landscape':
            self.__set_height()
            
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, new_height):
        if self.orientation == 'portrait':
            self.__set_height()
        if self.orientation == 'landscape':
            self.__set_width()

    def __set_height(self):
        page_height = (self.pageDim[self._pagesize]).height
        self._width = page_height - (2 * self._top)

    def __set_width(self):
        page_width = (self.pageDim[self._pagesize]).width
        self._width = page_width - (2 * self._left)
    

