void merge(vector<int> &a, vector<int> &b)
{
    int n = a.size();
    int m = b.size();
    int total_len = n + m;
    int gap = (total_len / 2) + total_len % 2;
    while (gap > 0)
    {
        int i = 0, j = gap;
        while (j < total_len)
        {
            /* comparing elements in first array - if b[j]<a[i] swap their values */
            if (j < n && a[i] > a[j])
                swap(a[i], a[j]);

            /* comparing elements in both arrays */
            else if (j >= n && i < n && a[i] > b[j - n])
                swap(a[i], b[j - n]);

            /* comparing elements in the second array */
            else if (j >= n && i >= n && b[i - n] > b[j - n])
                swap(b[i - n], b[j - n]);

            j++;
            i++;
        }
        gap = gap <= 1 ? 0 : (gap / 2) + (gap % 2);
    }
}