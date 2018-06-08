import ipywidgets as ipw

def get_start_widget(appbase, jupbase, notebase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <tr>
        <th style="text-align:center"></th>
        <th style="width:70px" rowspan=2></th>
        <th style="text-align:center"></th>
    <tr>
    <td valign="top"><ul>
    <li><a href="{appbase}/setup_computer.ipynb" target="_blank">Setup Connection to Quantum-Mobile</a>
    </ul></td>
    
    <td valign="top"><ul>
    <li><a href="{appbase}/setup_code.ipynb" target="_blank">Setup Codes</a>
    </ul></td>

    </tr></table>
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase, notebase=notebase)
    return ipw.HTML(html)
    
#EOF
