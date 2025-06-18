# Notes

```bash
-> % sudo bpftrace -f json ./blk.bt
{"type": "attached_probes", "data": {"probes": 4}}
{"type": "printf", "data": "Tracing key VFS calls... Hit Ctrl-C to end.\n"}
{"type": "time", "data": "13:13:15\n"}
{"type": "map", "data": {"@": {"32768": 1, "24576": 1, "0": 2, "16384": 2, "4096": 2}}}
{"type": "time", "data": "13:13:16\n"}
{"type": "time", "data": "13:13:17\n"}
{"type": "map", "data": {"@": {"4096": 1}}}
{"type": "time", "data": "13:13:18\n"}
{"type": "time", "data": "13:13:19\n"}
{"type": "time", "data": "13:13:20\n"}
{"type": "map", "data": {"@": {"32768": 1, "24576": 1, "8192": 1, "0": 2, "12288": 2, "16384": 5, "4096": 136}}}
{"type": "time", "data": "13:13:21\n"}
{"type": "time", "data": "13:13:22\n"}
{"type": "time", "data": "13:13:23\n"}
{"type": "time", "data": "13:13:24\n"}
{"type": "map", "data": {"@": {"32768": 1, "0": 2, "16384": 2, "4096": 3}}}
{"type": "time", "data": "13:13:25\n"}
{"type": "map", "data": {"@": {"114688": 1, "81920": 1, "8192": 1, "131072": 2, "49152": 4, "32768": 8, "0": 32, "4096": 35, "16384": 142}}}
{"type": "time", "data": "13:13:26\n"}
{"type": "time", "data": "13:13:27\n"}
{"type": "map", "data": {"@": {"16384": 1, "8192": 2, "4096": 91}}}
{"type": "time", "data": "13:13:28\n"}
{"type": "time", "data": "13:13:29\n"}
{"type": "time", "data": "13:13:30\n"}
{"type": "time", "data": "13:13:31\n"}
{"type": "time", "data": "13:13:32\n"}
{"type": "map", "data": {"@": {"32768": 1, "16384": 2}}}
{"type": "time", "data": "13:13:33\n"}
{"type": "map", "data": {"@": {"16384": 1, "0": 2, "8192": 2, "564": 3, "512": 9, "4096": 96}}}
```
