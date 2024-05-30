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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var client = new RestClient();
            var url = "https://www.affirmations.dev/";
            var request = new RestRequest(url, Method.Get);
            RestResponse response = client.Get(request);
            richTextBox1.Text = response.Content;

        }
    }
}
