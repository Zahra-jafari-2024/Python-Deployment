using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace WindowsFormsApp1
{
    public partial class dictionary : Form
    {
        public dictionary()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var client = new RestClient();
            var url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + textBox1.Text;
            var request = new RestRequest(url, Method.Get);
            RestResponse response = client.Get(request);
            richTextBox1.Text = response.Content;

        }
    }
}
