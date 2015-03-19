
# coding: utf-8

# ### Short Answer Response

# In[ ]:

get_ipython().run_cell_magic(u'HTML', u'', u'<!DOCTYPE html>\n<html>\n    <head>\n        <style> \n            \n        </style>\n    </head>\n\n    <body>\n        \n        <div>\n            <textarea class="shortAnswer" id="R1" rows="10" cols="500" placeholder="Enter your response here...">\n            </textarea>\n            \n        </div>\n        <div>\n            <input type="submit" value="Save" />\n        </div>    \n        \n        \n        <!-- COMMENT: Where our Javascript begins. -->\n        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jsxgraph/0.98/jsxgraphcore.js"></script>\n        <script type=\'text/javascript\'>\n            \n            //Standard edX JSinput functions\n            getInput = function(){\n                state = {};\n                statestr = JSON.stringify(state);\n                console.log(statestr)\n                \n                //IPython Notebook Considerations\n                document.getElementById(\'spaceBelow\').innerHTML += \'<br>\'+statestr;\n                var command = "state = \'" + statestr + "\'";\n                console.log(command);\n\n                //Kernel\n                var kernel = IPython.notebook.kernel;\n                kernel.execute(command);\n\n                return statestr;\n            }\n\n            getState = function(){\n                state = {\'input\': JSON.parse(getInput())};\n                statestr = JSON.stringify(state);\n                return statestr\n            }\n\n            setState = function(statestr){\n                $(\'#msg\').html(\'setstate \' + statestr);\n                state = JSON.parse(statestr);\n                console.log(statestr);\n                console.debug(\'State updated successfully from saved.\');\n            }\n            \n            \n        </script>\n    </body>\n</html>')


# In[ ]:



